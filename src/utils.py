import os
from datetime import datetime
import pandas as pd

#  Save the experimental report to a CSV file
def save_exp_report(exp_report_file, config, nation, prompt, results):
    # Extract the directory part from the file path
    exp_report_path = os.path.dirname(exp_report_file)

    # Create the directory if it doesn't exist
    if not os.path.exists(exp_report_path):
        os.makedirs(exp_report_path)

    columns = ['timestamp']
    values = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]

    # Retrieve the keys and values of the configuration file
    for key, value in config.items():
        columns.append(key)
        values.append(str(value))

    # Save prompt
    columns.append('prompt')
    values.append(str(prompt))

    # Retrieve the keys and values of experimental results 
    for key, value in results.items():
        columns.append(key)
        values.append(value)
    
    # append accuracy metric
    columns.append('accuracy')
    values.append(accuracy_metric(nation, results))

    # Save report to CSV file
    if os.path.exists(exp_report_file):
        df_report = pd.read_csv(exp_report_file)
    else:
        df_report = pd.DataFrame(columns=columns)
    df_report.loc[len(df_report)] = values
    df_report.to_csv(exp_report_file, index=False)
    return df_report

# Check if experimental results exist for the given configuration
def exists_exp_report(save_path, config):
    if not os.path.exists(save_path):
        return False

    df_report = pd.read_csv(save_path)

    for index, result in df_report.iterrows():
        existence_flag = True
        for key, value in config.items():
            result_item = result[key]

            if result_item != value:
                existence_flag = False
                break

        if existence_flag == True:
            break

    return existence_flag

def accuracy_metric(nation, result):
    nation_value = result.get(nation, 0)
    total_value = sum(result.values())
    
    if total_value == 0:
        return 0
    
    accuracy = round((nation_value / total_value) * 100, 2)
    return accuracy

