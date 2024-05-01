import pandas as pd
from datasets import load_dataset

class DataModule:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.data_frame = self.load_data()

    def load_data(self):
        """Load dataset (only using datasets)"""
        return pd.DataFrame(load_dataset(self.dataset_name)['train'])

    def generate_questions(self, prompt):
        df = self.data_frame
        prompts = [
            f"{prompt} ### Question: {row.q}\n### Option A: {row.us}\n### Option B: {row.ko}\n### Response:"
            for _, row in df.iterrows()
        ]
        return prompts
    
    def prepare_for_choice(self, prompt, answers): #TODO 수정
        self.data_frame['answer'] = answers
        """Prepare data for choosing between options."""
        prompts = [
            "{} ### Question: {}\n### Option A: {}\n### Option B: {}\n### Response: {}\n### Answer:".format(
        prompt,row.q, row.us, row.ko, row.answer
            ) for _, row in self.data_frame.iterrows()
        ]
        return prompts