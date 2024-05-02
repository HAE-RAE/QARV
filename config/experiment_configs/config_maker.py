import yaml

base_config_path = './base_config.yml'
model_names_path = './model_names.yml'

with open(base_config_path, 'r') as file:
    base_config = yaml.safe_load(file)

with open(model_names_path, 'r') as file:
    model_names = yaml.safe_load(file)

for i, model_name in enumerate(model_names):
    base_config['model_ckpt'] = model_name
    new_config_path = f'./config_{i+1}.yml'

    with open(new_config_path, 'w') as file:
        yaml.safe_dump(base_config, file, default_flow_style=False, allow_unicode=True)

print("done!")
