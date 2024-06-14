import json

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


