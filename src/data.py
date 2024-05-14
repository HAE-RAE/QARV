import pandas as pd
from datasets import load_dataset
import random

class DataModule:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.data_frame = self.load_data()
        self.generate_options()

    def load_data(self):
        """Load dataset (only using datasets)"""
        return pd.DataFrame(load_dataset(self.dataset_name)['train'])

    def generate_options(self):
        options_list = [{'a': 'us', 'b': 'ko'}, {'a': 'ko', 'b': 'us'}]
        self.data_frame['opt'] = self.data_frame.apply(lambda x: random.choice(options_list), axis=1)

    def generate_questions(self, prompt, exp):
        df = self.data_frame
        template = "{prompt} ### Question: {q}\n### Option A: {a}\n### Option B: {b}\n### Response:"
        if 'sc' in exp:
            k = int(exp.split('-')[-1])
            df = pd.DataFrame({
                'q': [q for q in df['q'] for _ in range(k)],
                'us': [us for us in df['us'] for _ in range(k)],
                'ko': [ko for ko in df['ko'] for _ in range(k)],
            })
            self.data_frame = df
            template += " Let’s think step by step."

        prompts = [
            template.format(
                prompt=prompt,
                q=row.q,
                a=row.us if row.opt['a'] == 'us' else row.ko,
                b=row.us if row.opt['b'] == 'us' else row.ko
            )
            for _, row in df.iterrows()
        ]
        return prompts

    def prepare_for_choice(self, prompt, answers):
        self.data_frame['answer'] = answers
        """Prepare data for choosing between options."""
        prompts = [
            "{} ### Question: {}\n### Option A: {}\n### Option B: {}\n### Response: {}\n### Answer: Option ".format(
                prompt, row.q,
                row.us if row.opt['a'] == 'us' else row.ko,
                row.us if row.opt['b'] == 'us' else row.ko,
                row.answer
            ) for _, row in self.data_frame.iterrows()
        ]
        return prompts
