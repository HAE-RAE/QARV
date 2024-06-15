#!/bin/bash

# Define an array of model names
MODELS=(
    "Qwen/Qwen1.5-32B"
    "Qwen/Qwen1.5-32B-Chat"
    "Qwen/Qwen1.5-72B"
    "Qwen/Qwen1.5-72B-Chat"
    "Qwen/Qwen1.5-110B"
    "Qwen/Qwen1.5-110B-Chat"
    "01-ai/Yi-34B"
    "01-ai/Yi-34B-Chat"
    "beomi/Yi-Ko-34B"
    "LLM360/K2"
) # Add more models as needed

# Loop through each model name in the array
for MODEL in "${MODELS[@]}"
do
  echo "Evaluating model: $MODEL"
  # huggingface-cli login --token "[HF_TOKEN]"
  python evaluate.py --model_name "$MODEL" --output_path "results"
  rm -rf ~/.cache/huggingface
  echo "Evaluation complete for model: $MODEL"
done
