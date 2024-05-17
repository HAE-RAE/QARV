import pandas as pd
from datasets import load_dataset
import random


class DataModule:
    def __init__(self, dataset_name, dataset_subset=None):
        self.dataset_name = dataset_name
        self.dataset_subset = dataset_subset
        self.data_frame = self.load_data()
        self.generate_options()

    def load_data(self):
        """Load dataset (only using datasets)"""
        if self.dataset_subset:
            return pd.DataFrame(load_dataset(self.dataset_name, self.dataset_subset)['test'])
        return pd.DataFrame(load_dataset(self.dataset_name)['test'])

    def generate_options(self):
        options_list = [{'a': 'us', 'b': 'ko'}, {'a': 'ko', 'b': 'us'}]
        self.data_frame['opt'] = self.data_frame.apply(lambda x: random.choice(options_list), axis=1)

    def generate_questions(self, prompt, exp):
        df = self.data_frame
        template = "{} ### Question: {}\n### Option A: {}\n### Option B: {}\n### Response:"
        if 'sc' in exp:
            k = int(exp.split('-')[-1])
            df = pd.DataFrame({
                    'q': [q for q in df['q'] for _ in range(k)],
                    'us': [q for q in df['us'] for _ in range(k)],
                    'ko': [q for q in df['ko'] for _ in range(k)],
                })
            self.data_frame = df
            template += " Let’s think step by step."
        prompts = []
        for _, row in df.iterrows():
            a_option = row['us'] if row['opt']['a'] == 'us' else row['ko']
            b_option = row['us'] if row['opt']['b'] == 'us' else row['ko']
            prompt_text = template.format(
                prompt,
                row['q'],
                a_option,
                b_option
            )
            prompts.append(prompt_text)
        return prompts

    def prepare_for_choice(self, prompt, answers):  # TODO 수정
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
