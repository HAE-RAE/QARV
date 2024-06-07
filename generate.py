from vllm import LLM, SamplingParams
from transformers import AutoTokenizer, AutoModelForCausalLM
import pandas as pd
from data import compile_prompt
import torch
from tqdm import tqdm
from more_itertools import chunked

def get_next_token_batch(model, tokenizer, prompts, options, bs, device):
    next_tokens = [answer for chunk in tqdm(chunked(prompts,bs),total=int(round(len(prompts)/bs))) for answer in get_next_token(model,tokenizer,chunk,options,device)]
    return next_tokens
    
def get_next_token(model, tokenizer, prompts, options, device):
    inputs = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True).to(device)

    # Get logits of the next token
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    indices = tokenizer.convert_tokens_to_ids(options)

    # Determine the most likely next token
    next_tokens = []
    for logit in logits[:, -1, :]:  # iterate over logits for the last token position in each sequence
        top_index = torch.argmax(logit[indices])  # find the max logit value over the indices of options
        next_tokens.append(options[top_index.item()])

    del inputs
    del logits
    torch.cuda.empty_cache()
    return next_tokens

def generate_queries(df, lang, targets, prompts, cot_mode=False):
    queries = []
    for tgt in targets:
        for pmt in prompts:
            queries.extend([compile_prompt(row.q, row.us, row.ko, lang, tgt, pmt, cot_mode) for _, row in df.iterrows()])
    return queries

def generate_llm_outputs(llm, queries):
    sampling_params = SamplingParams(temperature=0.8, top_p=0.95, min_tokens=20, max_tokens=1024)
    outputs = llm.generate([item['query'] for item in queries], sampling_params)
    return [output.outputs[0].text for output in outputs]