from collections import Counter
import outlines

class ExperimentModule:
    def __init__(self, data_module, model_module):
        self.data_module = data_module
        self.model_module = model_module
        self.model = self.model_module.load_outlines_model()

    def run_experiment(self, prompt, sampling_params, exp=None): 
        if exp == "cot" or exp == "sc":
            # Chain-of-Thought & Self-Consistency Voting
            questions = self.data_module.generate_questions(prompt, exp)
            answers = self.model_module.generate_answers(questions, sampling_params)
            generator = outlines.generate.choice(self.model, ['A', 'B'])
            choice_questions = self.data_module.prepare_for_choice(prompt, answers)
            final_answers = generator(choice_questions)
            if exp == 'sc':
                final_answers = [Counter(final_answers[i:i+3]).most_common()[0][0] for i in range(0, len(final_answers), 3)]
            results = self.count_answers(final_answers, self.data_module.data_frame['opt'])
        else:
            # multiple choice
            questions= self.data_module.generate_questions(prompt, exp)
            generator = outlines.generate.choice(self.model, ['A', 'B'])
            final_answers = generator(questions)
            results = self.count_answers(final_answers, self.data_module.data_frame['opt'])
        return results

    @staticmethod
    def count_answers(answers, options):
        us_count = ko_count = 0

        for answer, option in zip(answers, options):
            selected = option[answer.lower()]
            us_count += selected == 'us'
            ko_count += selected == 'ko'

        return {'US': us_count, 'KO': ko_count}
