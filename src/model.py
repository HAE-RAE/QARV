from vllm import LLM, SamplingParams
from outlines import models
import torch
from transformers import AutoModelForCausalLM

class ModelModule:
    def __init__(self, model_ckpt, gpu_args, use_vllm, model_branch = None):
        self.tensor_parallel_size = self._check_parallel_devices(gpu_args)
        self.model_branch = model_branch
        self.model_ckpt = model_ckpt
        self.use_vllm = use_vllm
        self.model = self.load_model()
        
    def load_model(self):
        """Load LLM """
        if self.use_vllm == False:
            llm = AutoModelForCausalLM.from_pretrained(self.model_ckpt, revision = self.model_branch)
        else:
            llm = LLM(model = self.model_ckpt, tensor_parallel_size=self.tensor_parallel_size, revision = self.model_branch, tokenizer_revision = self.model_branch)
        return llm
    
    def load_outlines_model(self):
        if self.use_vllm==True:
            llm = models.VLLM(self.model)
        else: 
            if self.model_branch == None:
                llm = models.transformers(model_name = self.model_ckpt)
            else:
                model_kwargs = {"revision": self.model_branch}
                llm = models.transformers(model_name = self.model_ckpt, model_kwargs = model_kwargs)
        return llm

    def generate_answers(self, questions, sampling_params):
        outputs = self.model.generate(questions, sampling_params)
        return [output.outputs[0].text for output in outputs]
    
    def _check_parallel_devices(self, gpu_args):
        if gpu_args == 'auto':
            num_gpus = torch.cuda.device_count()
        else:
            num_gpus = gpu_args
        return int(num_gpus)


