#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Define an array of models
MODELS=("42dot/42dot_LLM-SFT-1.3B" "Qwen/Qwen1.5-0.5B-Chat")

# Loop through each model
for MODEL in "${MODELS[@]}"
do
    echo "Running scripts for model: $MODEL"
    
    echo "Running generate_query.py"
    python generate_query.py --model $MODEL

    echo "Running generate_final_answer.py"
    python generate_final_answer_multi.py --model $MODEL --custom_batch_size 16

    echo "Running evaluate.py"
    python evaluate.py --model $MODEL

    echo "Scripts executed successfully for model: $MODEL"
    echo "-----------------------------------------"
done

echo "All models processed."