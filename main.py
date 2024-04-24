from src.data import DataModule
from src.model import ModelModule
from src.experiment import ExperimentModule
from src.analysis import AnalysisModule
from vllm import SamplingParams

def main():
    # TODO : dataset_name 및 model_ckpt는 argument로 받도록
    dataset_name = "HAERAE-HUB/QARV-binary"
    model_ckpt = "yanolja/EEVE-Korean-Instruct-10.8B-v1.0"

    # Module Initialization
    data_module = DataModule(dataset_name)
    model_module = ModelModule(model_ckpt)

    # TODO : 이것도 yaml같은걸로 받도록 구현하면 좋을듯 
    prompts = [
        "Answer as if you are a native speaker of Korean.",
        "Answer as if you are a native speaker of English."
    ]

    # Sampling parameters
    sampling_params = SamplingParams(
        temperature=0.8,
        top_p=0.95,
        min_tokens=20,
        max_tokens=1024,
        stop=['###', '#', '\n\n', '\n']
    )

    # experiment
    for prompt in prompts:
        experiment_module = ExperimentModule(data_module, model_module)
        results = experiment_module.run_experiment(prompt, sampling_params)
        analysis_module = AnalysisModule(results)
        report = analysis_module.generate_report()
        print(f"Results for prompt: '{prompt}'")
        print(report)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
