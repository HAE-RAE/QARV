from src.utils import save_exp_report
import os

class AnalysisModule:
    def __init__(self, config, prompt, results):
        self.config = config
        self.prompt = prompt
        self.results = results

    def generate_report(self, exp_result_file):
        """Generate and save a report"""
        report = save_exp_report(exp_result_file, self.config, self.prompt, self.results)
        return report
