from src.data import DataModule
from src.model import ModelModule
from src.experiment import ExperimentModule
from src.analysis import AnalysisModule
import torch
from vllm import SamplingParams
import yaml
from config import args

# Load configuration from YAML
def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main(args, config, prompts, gpu_args):
    # Module Initialization
    data_module = DataModule(config['dataset_name'])
    model_module = ModelModule(config['model_ckpt'], gpu_args=gpu_args)

    # Sampling parameters
    sampling_params = SamplingParams(**config['sampling_params'])

    # Experiment
    for prompt in prompts:
        experiment_module = ExperimentModule(data_module, model_module)
        results = experiment_module.run_experiment(prompt, sampling_params)
        analysis_module = AnalysisModule(config, prompt, results)
        report = analysis_module.generate_report(args.exp_report_file)
        print(f"Results for prompt: '{prompt}'")
        print(report)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    args_cli = args.get_args()
    config = load_config(args_cli.config_file)
    prompts = load_config(args_cli.prompts_file)
    gpu_args = args_cli.num_gpus
    print(config)
    print(prompts)

    main(args_cli, config, prompts, gpu_args)
