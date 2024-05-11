# QARV Experiment

## Project Overview
The QARV (Question and Answers with Regional Variance) project aims to curate a collection of questions with answers that exhibit regional variations across different nations.

## Modules
The project is divided into several modules to facilitate easy management and scalability:
- `DataModule`: Handles data loading and preprocessing.
- `ModelModule`: Manages model configuration, loading, and execution.
- `ExperimentModule`: Conducts experiments and gathers results.
- `AnalysisModule`: Analyzes the experiment results and generates reports.

## Installation
To set up this project, follow these steps:

### Prerequisites
- Python 3.8 or higher
- pip
- Access to a terminal or command-line interface
- CUDA 

### Cloning the Repository
Clone the repository to your local machine using:

```bash
git clone https://github.com/HAETAE-project/QARV
```
### Dependencies
Install all required dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

### Experiment Settings
1. In 'config/config.yaml', enter the dataset and model ckpt to use, and enter the hyperparameters for generation  

2. In 'config/prompt.yaml', enter all the prompts you want to use in your experiment.  


### Usage 

```bash
python main.py --config_file ./config/my_config.yml --prompts_file ./config/my_prompts.yml --exp_report_file ./exp/my_results.csv --num_gpus "auto" --exp sc
```

### Arguments
The following command-line arguments are available for configuring the QARV experiment:

**--config_file** : Specifies the path to the configuration YAML file.  
Type: str  
Default: ./config/config.yml  
Usage: --config_file PATH  

**--prompts_file** : Specifies the path to the prompts YAML file.
Type: str  
Default: ./config/prompt.yml  
Usage: --prompts_file PATH  

**--exp_report_file** : Specifies the path to the experimental results file.  
Type: str  
Default: ./exp/report.csv  
Usage: --exp_report_file PATH  

**--num_gpus** : Specifies the number of GPUs to use for distributed inference.  
Type: str  
Default: auto  
Usage: --num_gpus NUMBER  

**--exp** : Specifies which experiment to run. This option allows the selection of different experimental setups.  
Type: str  
Default: None  
Usage: --exp EXPERIMENT_OPTION(only "sc" is provided now)  

**--model_cache_dir** : Specifies the directory for caching models and other data used by Hugging Face libraries.   
Type: str    
Default: None     
Usage: --model_cache_dir PATH_TO_CACHE_DIRECTORY    

**--use_vllm** : Specifies whether to use a very large language model (vLLM) for inference.   
Type: bool    
Default: True    
Usage: --use_vllm true or false    

**--model_branch** : Used to specify a particular model branch on the Hugging Face platform when you want to utilize models other than the main branch.    
Type: str  
Default: None    
Usage: --model_branch BRANCH_NAME    
                                 
## Contributing

We welcome contributions to this project! For detailed guidelines on how to contribute, please refer to our [Contribution Pages](https://github.com/guijinSON/QARV/tree/main).

