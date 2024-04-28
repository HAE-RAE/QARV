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

### Dependencies
Install all required dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

### Cloning the Repository
Clone the repository to your local machine using:

```bash
git clone https://github.com/HAETAE-project/QARV
```

### Usage 

```bash
python main.py --dataset_name "HAERAE-HUB/QARV-binary" --model_ckpt "yanolja/EEVE-Korean-Instruct-10.8B-v1.0" --num_gpus "auto"

```

## Contributing

We welcome contributions to this project! For detailed guidelines on how to contribute, please refer to our [Contribution Pages](https://github.com/guijinSON/QARV/tree/main).

