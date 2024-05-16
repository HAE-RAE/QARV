from collections import Counter
import outlines
from evaluate import load
from src.utils import accuracy_metric  # utils 모듈에서 accuracy_metric 함수 가져오기

class ExperimentModule:
    def __init__(self, data_module, model_module):
        self.data_module = data_module
        self.model_module = model_module
        self.model = self.model_module.load_outlines_model()

    def run_experiment(self, prompt, sampling_params, exp=None):
        bleu = load("bleu")
        results = {}  # results 딕셔너리 초기화

        if exp == "cot" or "sc" in exp:
            # Chain-of-Thought & Self-Consistency Voting
            questions = self.data_module.generate_questions(prompt, exp)
            answers = self.model_module.generate_answers(questions, sampling_params)
            generator = outlines.generate.choice(self.model, ['A', 'B'])
            choice_questions = self.data_module.prepare_for_choice(prompt, answers)
            final_answers = generator(choice_questions)

            Gen_answers = [answer.split("Response:")[-1].strip() for answer in answers]  # 실제 텍스트 답변 추출

            bleu_scores = []
            references = []
            category = []
            for gen_answer, final_answer, row in zip(Gen_answers, final_answers, self.data_module.data_frame.itertuples(index=False)):
                if final_answer == 'A':
                    reference = row.us
                else:
                    reference = row.ko
                bleu_score = bleu.compute(predictions=[gen_answer], references=[[reference]])['bleu']
                bleu_scores.append(bleu_score)
                references.append(reference)
                category.append(row.category)

            if "sc" in exp:
                k = int(exp.split('-')[-1])
                final_answers = [Counter(final_answers[i:i+k]).most_common()[0][0] for i in range(0, len(final_answers), k)]

            results.update(self.count_answers(final_answers, self.data_module.data_frame['opt']))  # results에 US, KO 개수 추가
            results['cot'] = answers
            results['generated_answers'] = final_answers
            results['questions'] = questions  # 질문 저장
            results['model_answer'] = Gen_answers
            results['references'] = references  # reference 추가
            results['bleu_scores'] = bleu_scores
            results['category'] = category # 카테고리 저장
        else:
            # multiple choice
            questions = self.data_module.generate_questions(prompt, exp)
            answers = self.model_module.generate_answers(questions, sampling_params)
            generator = outlines.generate.choice(self.model, ['A', 'B'])
            final_answers = generator(questions)

            Gen_answers = [answer.split("Response:")[-1].strip() for answer in answers]  # 실제 텍스트 답변 추출

            bleu_scores = []
            references = []
            category = []
            for gen_answer, final_answer, row in zip(Gen_answers, final_answers, self.data_module.data_frame.itertuples(index=False)):
                if final_answer == 'A':
                    reference = row.us
                else:
                    reference = row.ko
                bleu_score = bleu.compute(predictions=[gen_answer], references=[[reference]])['bleu']
                bleu_scores.append(bleu_score)
                references.append(reference)
                category.append(row.category)
            results.update(self.count_answers(final_answers, self.data_module.data_frame['opt']))  # results에 US, KO 개수 추가
            results['generated_answers'] = final_answers
            results['questions'] = questions  # 질문 저장
            results['model_answer'] = Gen_answers
            results['references'] = references  # reference 추가
            results['bleu_scores'] = bleu_scores
            results['category'] = category # 카테고리 저장
        # Calculate accuracy and add it to results
        nation = 'US' if 'us' in self.data_module.data_frame['opt'][0].values() else 'KO'
        accuracy = accuracy_metric(nation, results)
        results['accuracy'] = accuracy

        # Calculate average BLEU score and add it to results
        average_bleu = sum(bleu_scores) / len(bleu_scores) if bleu_scores else 0
        results['average_bleu'] = round(average_bleu * 100, 2)  # BLEU score also in percentage format

        return results

    @staticmethod
    def count_answers(answers, options):
        us_count = ko_count = 0

        for answer, option in zip(answers, options):
            selected = option[answer.lower()]
            us_count += selected == 'us'
            ko_count += selected == 'ko'

        return {'US': us_count, 'KO': ko_count}
