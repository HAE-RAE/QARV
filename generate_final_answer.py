from src import parse_arguments, load_config, write_output, load_data_from_file
from transformers import AutoTokenizer, AutoModelForCausalLM
from generate import get_next_token_batch

def update_queries_with_rationales(data_list, model, tokenizer, options, batch_size, device):
    prompts = [item['query'] for item in data_list]
    results = get_next_token_batch(model, tokenizer, prompts, options, batch_size, device)
    for dict_item, rationale in zip(data_list, results):
        dict_item['final_answer'] = rationale
    return data_list

def process_queries(file_path, model, tokenizer, options, batch_size, device):
    data_list = load_data_from_file(file_path)
    updated_queries = update_queries_with_rationales(data_list, model, tokenizer, options, batch_size, device)
    write_output(file_path, updated_queries)

def main():
    args = parse_arguments()
    config = load_config()    
    
    model_path = args.model
    default_path = f"{config['file_path']}/{model_path.split('/')[1]}.jsonl"
    cot_path = f"{config['file_path']}/{model_path.split('/')[1]}-cot.jsonl"

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
    batch_size = args.custom_batch_size if args.custom_batch_size > config['batch_size'] else config['batch_size']

    # Process default path
    process_queries(default_path, model, tokenizer, config['options'], batch_size, config['device'])

    # Process cot path
    process_queries(cot_path, model, tokenizer, config['options'], batch_size, config['device'])

if __name__ == "__main__":
    main()