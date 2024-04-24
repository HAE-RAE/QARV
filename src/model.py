from vllm import LLM, SamplingParams
from outlines import models

class ModelModule:
    def __init__(self, model_ckpt):
        self.model_ckpt = model_ckpt
        self.model = self.load_model()

    def load_model(self):
        """Load LLM """
        llm = LLM(self.model_ckpt)
        return models.VLLM(llm)

    def generate_answers(self, questions, sampling_params):
        outputs = self.model.generate(questions, sampling_params)
        return [output.outputs[0].text for output in outputs]
