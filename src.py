import json

<<<<<<< Updated upstream
def parse_arguments():
    parser = argparse.ArgumentParser(description='Model name.')
    parser.add_argument('--model', type=str, required=True, help='Model to use')
    parser.add_argument('--custom_batch_size', type=int, default=0, help='Custom batch size if needed')
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
            max_model_len = 512
        )
    
    return llm
    
def write_output(path, data):
    with open(path, 'w') as file:
        for dictionary in data:
            json.dump(dictionary, file)
            file.write('\n')
=======
def save_to_jsonl(data, filename):
    with open(filename, 'w') as file:
        for entry in data:
            json_string = json.dumps(entry)
            file.write(json_string + '\n')

def logprob_answer(logprob):
    for _,item in logprob.items():
        token = item.decoded_token.strip().upper()
        if token in ['A','B','C']:
            return token
        return 'C'
>>>>>>> Stashed changes

