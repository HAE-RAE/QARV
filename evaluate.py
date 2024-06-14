import argparse
from data import prepare_qrys
from vllm import LLM, SamplingParams
from src import save_to_jsonl, logprob_answer
import pandas as pd

parser = argparse.ArgumentParser(description="Run LLM model inference.")
parser.add_argument('--model_name', type=str, required=True, help='Name of the model to use for inference.')
parser.add_argument('--output_path', type=str, required=True, help='Path to save the output files.')

args = parser.parse_args()
model_name = args.model_name
model_dir = model_name.replace('/','_')
output_path = args.output_path

llm = LLM(model=model_name,tensor_parallel_size=torch.cuda.device_count(),max_model_len=2048)
direct_qrys, cot_qrys = prepare_qrys()
direct_sampling_params = SamplingParams(temperature=0.0, logprobs=20, max_tokens=5)
cot_sampling_params = SamplingParams(temperature=0.8, top_p=0.95, logprobs=20, min_tokens=20, max_tokens=512)


direct_outputs = llm.generate(
    [qry['query'] for qry in direct_qrys],
    direct_sampling_params
)

for item, output in zip(direct_qrys, direct_outputs):
    item['generation'] = output.outputs[0].text
    item['answer'] = logprob_answer(output.outputs[0].logprobs[0])

cot_outputs = llm.generate(
    [qry['query'] for qry in cot_qrys],
    cot_sampling_params
)

cot_answers = llm.generate(
    [qry['query'] + gen.outputs[0].text.strip() + "\n### Choose your final answer between A/B/C. \n### Answer:" for qry, gen in zip(cot_qrys, cot_outputs)],
    direct_sampling_params
)

for item, output, answer in zip(cot_qrys, cot_outputs, cot_answers):
    item['generation'] = output.outputs[0].text
    item['answer'] = logprob_answer(answer.outputs[0].logprobs[0])

save_to_jsonl(direct_qrys, f'{output_path}/{model_dir}-direct.jsonl')
save_to_jsonl(cot_qrys, f'{output_path}/{model_dir}-cot.jsonl')


direct_final = [] 
for item in cot_qrys:
    gold = item['answers'][item['target']]
    answer = item['answer']
    if gold==answer:acc=1
    else:acc=0
    direct_final.append([item['query'],item['language'],item['target'],item['prompt'],gold,answer,acc])
    
cot_final = [] 
for item in cot_qrys:
    gold = item['answers'][item['target']]
    answer = item['answer']
    if gold==answer:acc=1
    else:acc=0
    cot_final.append([item['query'],item['language'],item['target'],item['prompt'],item['generation'],gold,answer,acc])

direct_final_df = pd.DataFrame(direct_final,
                               columns=['query','language','target','prompt','gold','answer','acc']
                              )
cot_final_df = pd.DataFrame(cot_final,
                               columns=['query','language','target','prompt','generation','gold','answer','acc']
                              )

scores = []
for (lang,tgt),batch in direct_final_df.groupby(['language','target']):
        scores.append(["direct",lang,tgt,batch.acc.mean()])

for (lang,tgt),batch in cot_final_df.groupby(['language','target']):
        scores.append(["cot",lang,tgt,batch.acc.mean()])


df = pd.DataFrame(scores,columns=['type','language','target','score'])
df.to_csv(f'{output_path}/{model_dir}-results.csv',index=False)




