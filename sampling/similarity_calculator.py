import ast
import multiprocessing
import os
import random

import pandas as pd
from datasets import load_dataset
from rouge import Rouge
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm.contrib.concurrent import process_map


def load_data(seed, num_samples_slim_orca=40000):
    """
    Load or download the required datasets.

    This function checks if the datasets are already downloaded in the 'input' directory.
    If not, it downloads the datasets from the specified sources and saves them as CSV files.
    For the SlimOrca dataset, it performs random sampling to select a specified number of samples.

    Args:
        seed (int): Random seed for reproducibility.
        num_samples_slim_orca (int, optional): Number of samples to randomly select from the SlimOrca dataset.
            Default is 40000.

    Returns:
        tuple: A tuple containing the loaded datasets.
            - df_qarv (pd.DataFrame): The QARV dataset.
            - df_slim_orca (pd.DataFrame): The randomly sampled SlimOrca dataset.
            - df_kor_open_orca (pd.DataFrame): The KOR-OpenOrca-Platypus-v3 dataset.
    """

    os.makedirs('./input', exist_ok=True)
    os.makedirs('./output', exist_ok=True)
    os.makedirs('./inter', exist_ok=True)

    # QARV
    if not os.path.exists('input/QARV-binary-set.csv'):
        df_qarv = pd.DataFrame(load_dataset('HAERAE-HUB/QARV-binary-set')['train'])
        df_qarv.to_csv('./input/QARV-binary-set.csv', index=False)
    else:
        df_qarv = pd.read_csv('./input/QARV-binary-set.csv')

    # SlimOrca
    if not os.path.exists('./input/SlimOrca.csv'):
        df_slim_orca = pd.DataFrame(load_dataset("Open-Orca/SlimOrca")['train'])
        df_slim_orca.to_csv('./input/SlimOrca.csv', index=False)
    else:
        df_slim_orca = pd.read_csv('./input/SlimOrca.csv')

    # Random sampling and preprocessing for SlimOrca
    df_slim_orca = df_slim_orca.sample(n=num_samples_slim_orca, random_state=seed)
    df_slim_orca = df_slim_orca.apply(preproc_slim_orca, axis=1)
    df_slim_orca = df_slim_orca.reset_index(drop=True)
    df_slim_orca.to_csv('./inter/df_slim_orca.csv', index=False)

    # KorSlimOrca
    if not os.path.exists('./input/KOR-OpenOrca-Platypus-v3.csv'):
        df_kor_open_orca = pd.DataFrame(load_dataset("kyujinpy/KOR-OpenOrca-Platypus-v3")['train'])
        df_kor_open_orca.to_csv('./input/KOR-OpenOrca-Platypus-v3.csv', index=False)
    else:
        df_kor_open_orca = pd.read_csv('./input/KOR-OpenOrca-Platypus-v3.csv')

    print(f'##### Original QARV: {len(df_qarv)}, KorOpenOrca: {len(df_kor_open_orca)}, SlimOrca: {len(df_slim_orca)}')

    return df_qarv, df_slim_orca, df_kor_open_orca

def preproc_slim_orca(row):
    """
    Preprocess a row of the SlimOrca dataset.

    This function extracts the 'value' fields from the 'conversations' column of the SlimOrca dataset,
    specifically for rows where 'from' is 'human' or 'gpt'. The 'value' field from 'human' rows is assigned
    to the 'instruction' column, and the 'value' field from 'gpt' rows is assigned to the 'output' column.

    Args:
        row (pd.Series): A row from the SlimOrca dataset containing the 'conversations' column.

    Returns:
        pd.Series: A preprocessed row with 'instruction' and 'output' columns extracted from the 'conversations' column.
    """

    conversations = ast.literal_eval(row['conversations'])
    instruction = None
    answer = None

    for i in range(len(conversations)):
        if conversations[i]['from'] == 'human':
            instruction = conversations[i]['value']
            if i + 1 < len(conversations) and conversations[i + 1]['from'] == 'gpt':
                answer = conversations[i + 1]['value']
                break

    return pd.Series([instruction, answer], index=['instruction', 'output'])


def calc_avg_rouge_qarv(args):
    """
    Calculate the average Rouge score between a specific row and all rows in the QARV dataset.

    This function takes a tuple of arguments containing the row index, the row data, and the QARV dataset.
    It calculates the average Rouge score between the concatenated 'instruction' and 'output' fields of the row
    and the concatenated 'q', 'us', and 'ko' fields of each row in the QARV dataset.

    Args:
        args (tuple): A tuple containing the following elements:
            - idx (int): The index of the row.
            - row (pd.Series): The row data containing the 'instruction' and 'output' fields.
            - df_qarv (pd.DataFrame): The QARV dataset containing 'q', 'us', and 'ko' fields.

    Returns:
        tuple: A tuple containing the following elements:
            - idx (int): The index of the row.
            - avg_rouge (float): The average Rouge score between the row and all rows in the QARV dataset.
    """

    idx, row, df_qarv = args

    rouge = Rouge()
    instruction = row['instruction']
    output = row['output']
    text = str(instruction) + ' ' + str(output)

    avg_rouge = 0
    for _, qarv_row in df_qarv.iterrows():
        q = qarv_row['q']
        us = qarv_row['us']
        ko = qarv_row['ko']
        ref = q + ' ' + us + ' ' + ko
        scores = rouge.get_scores(text, ref)
        avg_rouge += scores[0]['rouge-l']['f']

    avg_rouge /= len(df_qarv)
    return idx, avg_rouge

def calc_avg_cossim_qarv(args):
    """
    Calculate the average cosine similarity between a specific row and all rows in the QARV dataset.

    This function takes a tuple of arguments containing the row index, the row data, and the QARV dataset.
    It calculates the average cosine similarity between the concatenated 'instruction' and 'output' fields of the row
    and the concatenated 'q', 'us', and 'ko' fields of each row in the QARV dataset. The cosine similarity is computed
    using the TF-IDF vectorization of the text data.

    Args:
        args (tuple): A tuple containing the following elements:
            - idx (int): The index of the row.
            - row (pd.Series): The row data containing the 'instruction' and 'output' fields.
            - df_qarv (pd.DataFrame): The QARV dataset containing 'q', 'us', and 'ko' fields.

    Returns:
        tuple: A tuple containing the following elements:
            - idx (int): The index of the row.
            - avg_cossim (float): The average cosine similarity between the row and all rows in the QARV dataset.
    """

    idx, row, df_qarv = args
    instruction = row['instruction']
    output = row['output']
    text = str(instruction) + ' ' + str(output)

    avg_cossim = 0
    for _, qarv_row in df_qarv.iterrows():
        q = qarv_row['q']
        us = qarv_row['us']
        ko = qarv_row['ko']
        ref = q + ' ' + us + ' ' + ko

        tfidf = TfidfVectorizer().fit_transform([text, ref])
        cossim = cosine_similarity(tfidf)[0][1]
        avg_cossim += cossim

    avg_cossim /= len(df_qarv)
    return idx, avg_cossim


if __name__ == "__main__":
    seed = 2024
    random.seed(seed)

    # Step 1. Download target dataset (SlimOrca/KorOpenOrca/QARV)
    num_samples_slim_orca = 40000  # SlimOrca sampling (40000)
    df_qarv, df_slim_orca, df_kor_open_orca = load_data(seed, num_samples_slim_orca)

    # Step 2. Calculate the average Rouge score between SlimOrca and QARV datasets
    pool = multiprocessing.Pool()
    results = process_map(calc_avg_rouge_qarv, [(args[0], args[1], df_qarv) for args in df_slim_orca.iterrows()],
                          total=len(df_slim_orca), chunksize=1)
    pool.close()
    pool.join()
    df_slim_orca['avg_rouge_qarv'] = [x[1] for x in sorted(results, key=lambda x: x[0])]
    df_slim_orca.to_csv('./inter/slim_orca_w_qarv.csv', index=False)

    # Step 3. Calculate the average Rouge score between KorOpenOrca and QARV datasets
    pool = multiprocessing.Pool()
    results = process_map(calc_avg_rouge_qarv, [(args[0], args[1], df_qarv) for args in df_kor_open_orca.iterrows()],
                          total=len(df_kor_open_orca), chunksize=1)
    pool.close()
    pool.join()
    df_kor_open_orca['avg_rouge_qarv'] = [x[1] for x in sorted(results, key=lambda x: x[0])]
    df_kor_open_orca.to_csv('./inter/kor_open_orca_w_qarv.csv', index=False)

    # Step 4. Calculate the average Cosine-Similarity score between SlimOrca and QARV datasets
    pool = multiprocessing.Pool()
    results = process_map(calc_avg_cossim_qarv, [(args[0], args[1], df_qarv) for args in df_slim_orca.iterrows()],
                          total=len(df_slim_orca), chunksize=1)
    pool.close()
    pool.join()
    df_slim_orca['avg_cossim_qarv'] = [x[1] for x in sorted(results, key=lambda x: x[0])]
    df_slim_orca.to_csv('./inter/slim_orca_w_qarv.csv', index=False)

    # Step 5. Calculate the average Cosine-Similarity score between KorOpenOrca and QARV datasets
    pool = multiprocessing.Pool()
    results = process_map(calc_avg_cossim_qarv, [(args[0], args[1], df_qarv) for args in df_kor_open_orca.iterrows()],
                          total=len(df_kor_open_orca), chunksize=1)
    pool.close()
    pool.join()
    df_kor_open_orca['avg_cossim_qarv'] = [x[1] for x in sorted(results, key=lambda x: x[0])]
    df_kor_open_orca.to_csv('./inter/kor_open_orca_w_qarv.csv', index=False)
