import pandas as pd
from datasets import load_dataset

class DataModule:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.data_frame = self.load_data()

    def load_data(self):
        """Load dataset (only using datasets)"""
        return pd.DataFrame(load_dataset(self.dataset_name)['train'])

    # def generate_questions(self, prompt):
    #     df = self.data_frame
    #     prompts = [
    #         f"{prompt} ### Question: {row.q}\n### Option A: {row.us}\n### Option B: {row.ko}\n### Response:"
    #         for _, row in df.iterrows()
    #     ]
    #     return prompts

    def generate_questions(self, prompts):
        df = self.data_frame
        formatted_prompts = []
        for _, row in df.iterrows():
            for prompt in prompts:
                formatted_prompt = (
                    f"{prompts[prompt]['context']} "
                    f"{prompts[prompt]['instruction']} "
                    f"Question: {prompts[prompt]['question']} "
                    f"{prompts[prompt]['response_placeholder']} "
                    f"### Question: {row.q}\n### Option A: {row.us}\n### Option B: {row.ko}\n### Response:"
                )
                formatted_prompts.append(formatted_prompt)
        return formatted_prompts