from collections import Counter

class ExperimentModule:
    def __init__(self, data_module, model_module):
        self.data_module = data_module
        self.model_module = model_module

    def run_experiment(self, prompt, sampling_params):
        questions = self.data_module.generate_questions(prompt)
        answers = self.model_module.generate_answers(questions, sampling_params)
        results = self.count_answers(answers)
        return results

    @staticmethod
    def count_answers(answers):
        """Count the frequency of answers and remap them for clarity!"""
        counts = dict(Counter(answers))
        return {'US': counts.get('Option A', 0), 'KO': counts.get('Option B', 0)}
