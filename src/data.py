import pandas as pd
from datasets import load_dataset

class DataModule:
    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
        self.data_frame = self.load_data()

    def load_data(self):
        """Load dataset (only using datasets)"""
        return pd.DataFrame(load_dataset(self.dataset_name)['train'])


    def generate_questions(self, prompt_config):
        df = self.data_frame
        formatted_prompts = []
        for _, row in df.iterrows():
            # Combine the prompt components with the question from the data frame
            formatted_prompt = (
                f"<|user|>\n"
                f"{prompt_config['context']}\n"
                f"{prompt_config['instruction']}\n\n"
                f"Question: {row['q']}\n\n"  # Replace 'q' with your actual question column name
                f"{prompt_config['response_placeholder']}"
            )
            formatted_prompts.append(formatted_prompt)
        return formatted_prompts