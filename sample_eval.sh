#!/bin/bash

python main.py --config_file ./config/experiment_configs/config_yi_6.yml --prompts_file ./config/prompt_en.yml --exp_report_file ./exp/yi_ko_6_EN.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset english

python main.py --config_file ./config/experiment_configs/config_yi_6.yml --prompts_file ./config/prompt_ko.yml --exp_report_file ./exp/yi_ko_6_KO.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset korean

python main.py --config_file ./config/experiment_configs/config_yi_34.yml --prompts_file ./config/prompt_en.yml --exp_report_file ./exp/yi_ko_34_EN.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset english

python main.py --config_file ./config/experiment_configs/config_yi_34.yml --prompts_file ./config/prompt_ko.yml --exp_report_file ./exp/yi_ko_34_KO.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset korean

python main.py --config_file ./config/experiment_configs/config_llama3_8.yml --prompts_file ./config/prompt_en.yml --exp_report_file ./exp/llama3_8_ko_EN.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset english

python main.py --config_file ./config/experiment_configs/config_llama3_8.yml --prompts_file ./config/prompt_ko.yml --exp_report_file ./exp/llama3_8_ko_KO.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset korean


python main.py --config_file ./config/experiment_configs/config_mistral.yml --prompts_file ./config/prompt_en.yml --exp_report_file ./exp/mistral_EN.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset english

python main.py --config_file ./config/experiment_configs/config_mistral.yml --prompts_file ./config/prompt_ko.yml --exp_report_file ./exp/mistral_KO.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset korean

python main.py --config_file ./config/experiment_configs/config_solar.yml --prompts_file ./config/prompt_en.yml --exp_report_file ./exp/solar_EN.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset english

python main.py --config_file ./config/experiment_configs/config_solar.yml --prompts_file ./config/prompt_ko.yml --exp_report_file ./exp/solar_KO.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset korean

python main.py --config_file ./config/experiment_configs/config_eeve.yml --prompts_file ./config/prompt_en.yml --exp_report_file ./exp/eeve_EN.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset english

python main.py --config_file ./config/experiment_configs/config_eeve.yml --prompts_file ./config/prompt_ko.yml --exp_report_file ./exp/eeve_KO.csv --num_gpus "auto" --exp_settings 'mc'  --dataset_subset korean

