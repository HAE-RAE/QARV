import logging
from collections import Counter
import outlines

class ExperimentModule:
    def __init__(self, data_module, model_module, logger = None):
        self.data_module = data_module
        self.model_module = model_module
        self.model = self.model_module.load_outlines_model()
        self.logger = logger or logging.getLogger(__name__)

    def run_experiment(self, prompt, sampling_params, exp=None):
        self.logger.info(f"Running experiment with prompt: {prompt} and exp: {exp}")
        if exp == "cot" or "sc" in exp:
            # Chain-of-Thought & Self-Consistency Voting
            self.logger.debug("Experiment type: Chain-of-Thought & Self-Consistency Voting")
            questions = self.data_module.generate_questions(prompt, exp)
            self.logger.debug(f"Generated questions: {questions}")
            
            answers = self.model_module.generate_answers(questions, sampling_params)
            self.logger.debug(f"Generated answers: {answers}")
            
            generator = outlines.generate.choice(self.model, ['A', 'B', 'C'])
            choice_questions = self.data_module.prepare_for_choice(prompt, answers)
            final_answers = generator(choice_questions)
            self.logger.debug(f"Final answers: {final_answers}")
            
            if "sc" in exp:
                k = int(exp.split('-')[-1])
                final_answers = [Counter(final_answers[i:i+k]).most_common()[0][0] for i in range(0, len(final_answers), k)]
                self.logger.debug(f"Self-consistency voting results: {final_answers}")
            results = self.count_answers(final_answers, self.data_module.data_frame['opt'],self.data_module.data_frame['category'])
        else:
            # multiple choice
            self.logger.debug("Experiment type: Multiple Choice")
            questions= self.data_module.generate_questions(prompt, exp)
            
            self.logger.debug(f"Generated questions: {questions}")
            generator = outlines.generate.choice(self.model, ['A', 'B', 'C'])
            final_answers = generator(questions)
            self.logger.debug(f"Final answers: {final_answers}")
            results = self.count_answers(final_answers, self.data_module.data_frame['opt'],self.data_module.data_frame['category'])
        self.logger.info(f"Experiment results: {results}")
        return results

    @staticmethod
    def count_answers(answers, options,categorys):
        us_count = ko_count = no_answer_count = 0
        us_dict = {f'US_{x}':0 for x in set(categorys)}
        ko_dict = {f'KO_{x}':0 for x in set(categorys)}
        no_dict = {f'NO_{x}':0 for x in set(categorys)}
        for answer, option, cate in zip(answers, options,categorys):
            selected = option.get(answer.lower())
            if selected == 'us':
                us_count += 1
                us_dict[f'us_{cate}'] += 1
            elif selected == 'ko':
                ko_count += 1
                ko_dict[f'ko_{cate}'] += 1
            else:
                no_answer_count += 1
                no_dict[f'no_{cate}'] += 1
        all_dict = dict(us_dict, **ko_dict)
        all_dict = dict(all_dict, **no_dict)
        return dict({'US': us_count, 'KO': ko_count, 'No_answer': no_answer_count}, **all_dict)

