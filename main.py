import argparse
import yaml
from src.data import DataModule
from src.model import ModelModule
from src.experiment import ExperimentModule
from src.analysis import AnalysisModule
from vllm import SamplingParams

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_name", type=str, required=True, help="Name of the dataset")
    parser.add_argument("--model_ckpt", type=str, required=True, help="Checkpoint of the model")
    parser.add_argument("--prompts_file", type=str, default="./prompts.yaml", help="Path to the prompts YAML file")
    args = parser.parse_args()

    # Module Initialization
    data_module = DataModule(args.dataset_name)
    model_module = ModelModule(args.model_ckpt)

    # Load prompts from YAML
    with open(args.prompts_file, 'r') as file:
        prompts = yaml.safe_load(file)

    # Sampling parameters
    sampling_params = SamplingParams(
        temperature=0.8,
        top_p=0.95,
        min_tokens=20,
        max_tokens=1024,
        stop=['###', '#', '\n\n', '\n']
    )

    # Experiment
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
