import argparse
from data import prepare_qrys, convert_to_chat_format
from vllm import LLM, SamplingParams
from src import save_to_jsonl, logprob_answer
import pandas as pd
import torch


### ---------------------------------- Arguments ---------------------------------- ###
parser = argparse.ArgumentParser(description="Run LLM model inference.")
parser.add_argument('--model_name', type=str, required=True, help='Name of the model to use for inference.')
parser.add_argument('--output_path', type=str, required=True, help='Path to save the output files.')
parser.add_argument('--model_revision', type=str, required=False, help='Revision of the model to use for inference.')
args = parser.parse_args()

model_dir = args.model_name.replace('/','_')
is_chat = False
if any(keyword in args.model_name.lower() for keyword in ('instruct', 'chat')):
    is_chat = True
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    print(tokenizer.chat_template)


### --------------------------- Model & Sampling Params ---------------------------- ###
llm = LLM(model=args.model_name, tensor_parallel_size=torch.cuda.device_count(), max_model_len=2048, revision=args.model_revision, disable_custom_all_reduce=True)
direct_sampling_params = SamplingParams(temperature=0.0, logprobs=5, max_tokens=5)
cot_sampling_params = SamplingParams(temperature=0.8, top_p=0.95, logprobs=5, min_tokens=20, max_tokens=512)


### ----------------------------------- Questions ----------------------------------- ###
direct_qrys, cot_qrys = prepare_qrys()
direct_questions = [qry['query'] for qry in direct_qrys]
cot_questions = [qry['query'] for qry in cot_qrys]
if is_chat:
    direct_questions = convert_to_chat_format(direct_questions, tokenizer)
    cot_questions = convert_to_chat_format(cot_questions, tokenizer)
    print(direct_questions[0])
    print(cot_questions[0])


### ----------------------------------- Generation ----------------------------------- ###
direct_outputs = llm.generate(direct_questions, direct_sampling_params)
cot_outputs = llm.generate(cot_questions, cot_sampling_params)

cot_final_questions = [qry['query'] + gen.outputs[0].text.strip() + "\n### Choose your final answer between A/B/C. \n### Answer:" for qry, gen in zip(cot_qrys, cot_outputs)]
if is_chat:
    cot_final_questions = convert_to_chat_format(cot_final_questions, tokenizer)
    print(cot_final_questions[0])
cot_answers = llm.generate(cot_final_questions, direct_sampling_params)

for item, output in zip(direct_qrys, direct_outputs):
    item['generation'] = output.outputs[0].text
    item['answer'] = logprob_answer(output.outputs[0].logprobs[0])

for item, output, answer in zip(cot_qrys, cot_outputs, cot_answers):
    item['generation'] = output.outputs[0].text
    item['answer'] = logprob_answer(answer.outputs[0].logprobs[0])

save_to_jsonl(direct_qrys, f'{args.output_path}/{model_dir}-direct.jsonl')
save_to_jsonl(cot_qrys, f'{args.output_path}/{model_dir}-cot.jsonl')


### ----------------------------------- Evaluation ----------------------------------- ###
direct_final = []
for item in direct_qrys:
    gold, answer = item['answers'][item['target']], item['answer']
    acc = 1 if gold == answer else 0
    direct_final.append([item['query'], item['language'], item['target'], item['prompt'], gold, answer, acc])

cot_final = []
for item in cot_qrys:
    gold, answer = item['answers'][item['target']], item['answer']
    acc = 1 if gold == answer else 0
    cot_final.append([item['query'], item['language'], item['target'], item['prompt'], item['generation'], gold, answer, acc])

direct_final_df = pd.DataFrame(direct_final, columns=['query', 'language', 'target', 'prompt', 'gold', 'answer', 'acc'])
cot_final_df = pd.DataFrame(cot_final, columns=['query', 'language', 'target', 'prompt', 'generation', 'gold', 'answer', 'acc'])

scores = []
for (lang, tgt), batch in direct_final_df.groupby(['language', 'target']):
    scores.append(['direct', lang, tgt, batch.acc.mean()])

for (lang, tgt), batch in cot_final_df.groupby(['language', 'target']):
    scores.append(['cot', lang, tgt, batch.acc.mean()])

df = pd.DataFrame(scores, columns=['type', 'language', 'target', 'score'])
df.to_csv(f'{args.output_path}/{model_dir}-results.csv', index=False)