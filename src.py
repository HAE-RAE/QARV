from vllm import LLM, SamplingParams
import json
import torch
import argparse
import yaml

def parse_arguments():
    parser = argparse.ArgumentParser(description='Model name.')
    parser.add_argument('--model', type=str, required=True, help='Model to use')
    return parser.parse_args()

def load_config(file_path='config.yaml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
        
def load_data_from_file(path):
    data_list = []
    with open(path, 'r') as file:
        for line in file:
            data = json.loads(line)
            data_list.append(data)
    return data_list

def initialize_vllm_model(model_path):
    
    llm = LLM(
            model=model_path, 
            tensor_parallel_size=torch.cuda.device_count(),
            max_model_len = 512
        )
    
    return llm
    
def write_output(path, data):
    with open(path, 'w') as file:
        for dictionary in data:
            json.dump(dictionary, file)
            file.write('\n')

