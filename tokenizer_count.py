import yaml
import logging
from transformers import AutoTokenizer
import os
import glob
import re

def is_korean_token(token):
    korean_regex = re.compile(r'[가-힣ㄱ-ㅎㅏ-ㅣ]+')
    return bool(korean_regex.search(token))

def get_korean_token_ratio(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    korean_token_count = 0
    total_token_count = 0
    
    for token_id in range(tokenizer.vocab_size):
        token = tokenizer.decode(token_id)
        cleaned_token = re.sub(r'\W', '', token)  
        if cleaned_token: 
            total_token_count += 1
            if is_korean_token(cleaned_token):  
                korean_token_count += 1
    
    if total_token_count == 0: 
        return 0
    korean_token_ratio = korean_token_count / total_token_count
    return korean_token_count, korean_token_ratio

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


file_handler = logging.FileHandler("korean_token_ratio.log")
file_handler.setLevel(logging.INFO)


formatter = logging.Formatter("%(asctime)s - %(message)s")
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)

config_folder = "./config/experiment_configs"

config_files = glob.glob(os.path.join(config_folder, "*.yml"))
print(config_files)
config_files.sort()

for config_path in config_files:
    config_name = os.path.basename(config_path)
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    model_names = config["model_ckpt"]
    logger.info(f"사용된 Config 파일: {config_name}")
    try:
        count, ratio = get_korean_token_ratio(model_names)
        logger.info(f"{model_names}의 한국어 토큰 비율: {ratio:.10f}")
        logger.info(f"{model_names}의 한국어 토큰 양: {count}")
    except:
        print(f"error at {model_names}")
        pass
    logger.info("=" * 50)  
