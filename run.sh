prompts_file='./config/prompt_addt.yml'

# 1 2 19 24 33 34 41 42 58 59
for config_idx in 1 2 19 24 33 34 41 42 58 59; do
  config_file='./config/experiment_configs/config_'$config_idx'.yml'
  exp_report_file='./exp/report_config_'$config_idx'_addt_prompts.csv'

  python -u main.py \
    --config_file $config_file \
    --prompts_file $prompts_file \
    --exp_report_file $exp_report_file \
    --num_gpus 'auto'
done
