MODEL_LIST=("yanolja/EEVE-Korean-Instruct-2.8B-v1.0" "daekeun-ml/phi-2-ko-v0.1")

for MODEL in "${MODEL_LIST[@]}"; do
    for LANG in "english" "korean"; do
        echo "Running evaluation for $MODEL - $LANG..."
        MODEL_BASENAME=$(basename "$MODEL")
        LANG_PREFIX=${LANG:0:2}
        python main.py --model_name "$MODEL" --prompts_file "./config/prompt_${LANG_PREFIX}.yml" --exp_report_file "./exp/${MODEL_BASENAME}_${LANG}.csv" --num_gpus "auto" --exp_settings "mc" --dataset_subset "$LANG"
    done
done
