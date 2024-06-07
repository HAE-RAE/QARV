import argparse
import json
import pandas as pd
from data import load_and_prepare_data
from src import initialize_vllm_model, write_output, parse_arguments, load_config
from vllm import LLM, SamplingParams
from generate import generate_queries, generate_llm_outputs


def main():
    args = parse_arguments()
    config = load_config()

    languages = config['languages']
    targets = config['targets']
    prompts = config['prompts']
    model_path = args.model

    default_path = f"{config['file_path']}/{model_path.split('/')[1]}.jsonl"
    cot_path = f"{config['file_path']}/{model_path.split('/')[1]}-cot.jsonl"

    all_queries = []
    for lang in languages:
        df = load_and_prepare_data(lang)
        all_queries.extend(generate_queries(df, lang, targets, prompts))
        
    write_output(default_path, all_queries)

    all_queries = []
    for lang in languages:
        df = load_and_prepare_data(lang)
        all_queries.extend(generate_queries(df, lang, targets, prompts, True))
        
    llm = initialize_vllm_model(model_path)
    output_texts = generate_llm_outputs(llm, all_queries)

    for dict_item, rationale in zip(all_queries, output_texts):
        dict_item['rationale'] = rationale

    write_output(cot_path, all_queries)

if __name__ == "__main__":
    main()

