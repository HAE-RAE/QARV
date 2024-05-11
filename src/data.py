import pandas as pd
from datasets import load_dataset
import random


class DataModule:
    def __init__(self, dataset_name, seed):
        self.dataset_name = dataset_name
        self.data_frame = self.load_data()
        self.seed = seed
        # self.options = self.generate_options(self.seed)

    def load_data(self):
        """Load dataset (only using datasets)"""
        return pd.DataFrame(load_dataset(self.dataset_name)['train'])

    def generate_options(self, seed):
        random.seed(seed)
        options_list = [{'a': 'us', 'b': 'ko'}, {'a': 'ko', 'b': 'us'}]
        self.data_frame['opt'] = random.choice(options_list, size=len(self.data_frame))

    def generate_questions(self, prompt, exp):
        df = self.data_frame
        template = "{prompt} ### Question: {q}\n### Option A: {a}\n### Option B: {b}\n### Response:"
        # template = "{prompt} ### Question: {q}\n### Option A: {opt_a}\n### Option B: {opt_b}\n### Response:"
        if exp == 'sc':
            df = pd.DataFrame({
                'q': [q for q in df['q'] for _ in range(3)],
                'us': [q for q in df['us'] for _ in range(3)],
                'ko': [q for q in df['ko'] for _ in range(3)],
            })
            self.data_frame = df
            template += " Let’s think step by step."

        prompts = [
            template.format_map({
                'prompt': prompt, 'q': row.q,
                'a': row.us if row.opt['a'] == 'us' else row.ko,
                'b': row.us if row.opt['b'] == 'us' else row.ko
            })
            for _, row in df.iterrows()
        ]
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
