import random
import pandas as pd
from datasets import load_dataset


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


template = """Return an answer between A/B/C.
### System Message: {}
### Question: {}
### Options: 
A. {}
B. {}
C. None of the above.
### Answer:"""


def format_question(row, language, target, prompt_type, cot=False):
    options = [(row['us'], 'us'), (row['ko'], 'ko')]
    random.shuffle(options)

    # Determine the correct and user response options
    answer_key = {options[0][1]:'A', options[1][1]:'B'}
    prompt_ = prompts[language][target][prompt_type]

    question = template.format(row['q'],prompt_,options[0][0],options[1][0])
    if cot:
        question += " Let's think step by step."
    
    question_dict = {
            'query': question,
            'options': {
                'A': options[0][0],
                'B': options[1][0],
                'C': 'None of the above'
            },
            'answers': answer_key,
            'language':language,
            'target':target,
            'prompt':prompt_type
        }

    return question_dict


def prepare_qrys():
    direct_qrys = []
    cot_qrys = []
    
    for lang in ['english','korean']:
        df = pd.DataFrame(
            load_dataset("HAERAE-HUB/QARV-binary-set", lang)['test']
        )
        
        for _, row in df.iterrows():
            for target in ['us','ko']:
                for prompt_type in ['na','qa','bio','rtf']:
                    direct_qrys.append(
                            format_question(row,lang,target,prompt_type)
                    )
                    cot_qrys.append(
                            format_question(row,lang,target,prompt_type,True)
                    )
                    
    return direct_qrys, cot_qrys


def convert_to_chat_format(questions, tokenizer):
    chat_questions = []  
    for question in questions:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        chat_questions.append(text)
    return chat_questions
