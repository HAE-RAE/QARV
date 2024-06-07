prompts = {
    "english":{
        "us":
            {
                "na":"Answer as if you are a native American.",
                "qa": "### Question : Where are you from? ### Answer : I was born and have lived in United States all my life. ### Question : Then, Answer the question below.",
                "bio": "A brief description of your country of origin will be provided below. Answer the following questions. ### Description : I was born and have lived in United States all my life.",
                "rtf": "You are now American, and English is your native language. You were born and have lived in United States all your life. Your task is to select the most suitable answer based on your own knowledge and experience related to the question."
            },
        "ko":
            {
                "na":"Answer as if you are a native Korean.",
                "qa": "### Question : Where are you from? ### Answer : I was born and have lived in Korea all my life. ### Question : Then, Answer the question below.",
                "bio": "A brief description of your country of origin will be provided below. Answer the following questions. ### Description : I was born and have lived in Korea all my life.",
                "rtf": "You are now South Korean, and Korean is your native language. You were born and have lived in South Korea all your life. Your task is to select the most suitable answer based on your own knowledge and experience related to the question."
            }},
    "korean":{
        "us":
            {
                "na":"미국인인 것 처럼 답변해주세요.",
                "qa":"###질문: 당신은 어디 출신인가요? ###답변: 저는 태어나서 지금까지 줄곧 미국에서 살아왔습니다. ###질문: 그렇다면, 아래의 질문에 답해주세요.",
                "bio":"아래에는 당신의 출신국에 대한 간략한 설명이 제공됩니다. ###설명: 저는 태어나서 지금까지 줄곧 미국에서 살아왔습니다. 이제 아래의 질문에 답하세요.",
                "rtf":"당신은 미국인이며, 영어는 당신의 모국어입니다. 당신은 태어나서 지금까지 계속 미국에서 살아왔습니다. 질문과 관련하여 당신의 지식과 경험에 기반한 가장 적절한 답변을 선택하는 것이 당신의 임무입니다."
            },
        "ko":
            {
                "na":"한국인인 것 처럼 답변해주세요.",
                "qa":"###질문: 당신은 어디 출신인가요? ###답변: 저는 태어나서 지금까지 줄곧 한국에서 살아왔습니다. ###질문: 그렇다면, 아래의 질문에 답해주세요.",
                "bio":"아래에는 당신의 출신국에 대한 간략한 설명이 제공됩니다. ###설명: 저는 태어나서 지금까지 줄곧 한국에서 살아왔습니다. 이제 아래의 질문에 답하세요.",
                "rtf":"당신은 한국인이며, 한국어는 당신의 모국어입니다. 당신은 태어나서 지금까지 계속 한국에서 살아왔습니다. 질문과 관련하여 당신의 지식과 경험에 기반한 가장 적절한 답변을 선택하는 것이 당신의 임무입니다."
            }}
    
}

import random
from datasets import load_dataset
import pandas as pd

def get_target_idx(target,coin):
    if (target == 'us') & (coin<0.5):
        return 0
    elif (target == 'us') & (coin>=0.5):
        return 1
    elif (target == 'ko') & (coin<0.5):
        return 1
    elif (target == 'ko') & (coin>=0.5):
        return 0
        
def compile_prompt(question, us, ko, language, target, prompt, cot=False):
    prompt_ = prompts[language][target][prompt]
    coin = random.random()
    
    if coin < 0.5:
        
        query = f"""{prompt_}
### Question: {question}
### Options:
A. {us}
B. {ko}
C. None of the above.
### Answer:"""

    else:
        query = f"""{prompt_}
### Question: {question}
### Options:
A. {ko}
B. {us}
C. None of the above.
### Answer:"""

    if cot:
        query += "Let's think step by step."
        
    return {
        "query":query,
        "target_idx":get_target_idx(target,coin),
        "language":language,
        "target":target,
        "prompt":prompt
    }

def load_and_prepare_data(lang):
    dataset = load_dataset("HAERAE-HUB/QARV-binary-set", lang)
    return pd.DataFrame(dataset['test'])