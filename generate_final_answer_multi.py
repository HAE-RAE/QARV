import torch
from multiprocess import set_start_method
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from src import parse_arguments, load_config, write_output, load_data_from_file

### -------------- Pre-define here for get_next_token_batch -------------- ###
args = parse_arguments()
config = load_config()

model_path = args.model
default_path = f"{config['file_path']}/{model_path.split('/')[1]}.jsonl"
cot_path = f"{config['file_path']}/{model_path.split('/')[1]}-cot.jsonl"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path).eval()
options = config['options']
indices = tokenizer.convert_tokens_to_ids(config['options'])
batch_size = args.custom_batch_size if args.custom_batch_size > config['batch_size'] else config['batch_size']
### ---------------------------------------------------------------------- ###


def get_next_token_batch(batch, rank):
    device = f"cuda:{(rank or 0) % torch.cuda.device_count()}"
    model.to(device)

    inputs = tokenizer(batch['prompts'], padding=True, truncation=True, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        
    next_tokens = []
    for logit in logits[:, -1, :]:  # iterate over logits for the last token position in each sequence
        top_index = torch.argmax(logit[indices])  # find the max logit value over the indices of options
        next_tokens.append(options[top_index.item()])
        
    batch['next_tokens'] = next_tokens
    return batch


def update_queries_with_rationales(data_list):
    prompts = [item['query'] for item in data_list]
    raw_dataset = Dataset.from_dict({'prompts': prompts})
    results = raw_dataset.map(
        get_next_token_batch,
        batched=True,
        batch_size=batch_size,
        with_rank=True,
        num_proc=torch.cuda.device_count(),
    )

    for dict_item, rationale in zip(data_list, results['next_tokens']):
        dict_item['final_answer'] = rationale
    return data_list


def process_queries(file_path):
    data_list = load_data_from_file(file_path)
    updated_queries = update_queries_with_rationales(data_list)
    write_output(file_path, updated_queries)


if __name__ == "__main__":
    set_start_method("spawn")
    
    # Process default path
    process_queries(default_path)

    # Process cot path
    process_queries(cot_path)