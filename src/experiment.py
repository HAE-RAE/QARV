from collections import Counter
import outlines
from evaluate import load
from src.utils import accuracy_metric  
from sklearn.metrics import precision_score, recall_score, f1_score

class ExperimentModule:
    def __init__(self, data_module, model_module):
        self.data_module = data_module
        self.model_module = model_module
        self.model = self.model_module.load_outlines_model()

    def run_experiment(self, prompt, sampling_params, exp=None):
        results = {}  

        if exp == "cot" or "sc" in exp:
            # Chain-of-Thought & Self-Consistency Voting
            questions = self.data_module.generate_questions(prompt, exp)
            answers = self.model_module.generate_answers(questions, sampling_params)
            generator = outlines.generate.choice(self.model, ['A', 'B'])
            choice_questions = self.data_module.prepare_for_choice(prompt, answers)
            final_answers = generator(choice_questions)

            Gen_answers = [answer.split("Response:")[-1].strip() for answer in answers]  # 실제 텍스트 답변 추출

            if "sc" in exp:
                k = int(exp.split('-')[-1])
                final_answers = [Counter(final_answers[i:i+k]).most_common()[0][0] for i in range(0, len(final_answers), k)]

            results.update(self.count_answers(final_answers, self.data_module.data_frame['opt']))  # results에 US, KO 개수 추가
            results['cot'] = answers
            results['generated_answers'] = final_answers
            results['questions'] = questions  # 질문 저장
            results['model_answer'] = Gen_answers

            # Calculate precision, recall, and f1-score
            true_labels = [row.us if row.us else row.ko for row in self.data_module.data_frame.itertuples(index=False)]
            pred_labels = ['US' if answer == 'A' else 'KO' for answer in final_answers]
            results['precision'] = precision_score(true_labels, pred_labels, pos_label='US')
            results['recall'] = recall_score(true_labels, pred_labels, pos_label='US')
            results['f1_score'] = f1_score(true_labels, pred_labels, pos_label='US')
        else:
            # multiple choice
            questions = self.data_module.generate_questions(prompt, exp)
            answers = self.model_module.generate_answers(questions, sampling_params)
            generator = outlines.generate.choice(self.model, ['A', 'B'])
            final_answers = generator(questions)

            Gen_answers = [answer.split("Response:")[-1].strip() for answer in answers]  # 실제 텍스트 답변 추출

            results.update(self.count_answers(final_answers, self.data_module.data_frame['opt']))  # results에 US, KO 개수 추가
            results['generated_answers'] = final_answers
            results['questions'] = questions  # 질문 저장
            results['model_answer'] = Gen_answers

            # Calculate precision, recall, and f1-score
            true_labels = [row.us if row.us else row.ko for row in self.data_module.data_frame.itertuples(index=False)]  
            pred_labels = ['US' if answer == 'A' else 'KO' for answer in final_answers]
            results['precision'] = precision_score(true_labels, pred_labels, pos_label='US')
            results['recall'] = recall_score(true_labels, pred_labels, pos_label='US')
            results['f1_score'] = f1_score(true_labels, pred_labels, pos_label='US')

        # Calculate accuracy and add it to results
        accuracy = accuracy_metric('US' if 'us' in self.data_module.data_frame['opt'][0].values() else 'KO', results)
        results['accuracy'] = accuracy

        return results

    @staticmethod
    def count_answers(answers, options):
        us_count = ko_count = 0

        for answer, option in zip(answers, options):
            selected = option[answer.lower()]
            us_count += selected == 'us'
            ko_count += selected == 'ko'

        return {'US': us_count, 'KO': ko_count}
