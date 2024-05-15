import os
import random

import matplotlib.pyplot as plt
import pandas as pd


def load_data():
    # SlimOrca
    if os.path.exists('./inter/slim_orca_w_qarv.csv'):
        df_slim_orca = pd.read_csv('./inter/slim_orca_w_qarv.csv')
    else:
        raise FileNotFoundError(
            "File './inter/slim_orca_w_qarv.csv' not found. Please run similarity_calculator.py first.")

    # KorSlimOrca
    if os.path.exists('./inter/kor_open_orca_w_qarv.csv'):
        df_kor_open_orca = pd.read_csv('./inter/kor_open_orca_w_qarv.csv')
    else:
        raise FileNotFoundError(
            "File './inter/kor_open_orca_w_qarv.csv' not found. Please run similarity_calculator.py first.")

    return df_slim_orca, df_kor_open_orca


def plot_histogram(data, title, xlabel, ylabel, filename):
    plt.hist(data, bins=20)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt.show()


def filter_dataset(df, target, th, filename):
    df_filtered = df[df[target] <= th]
    df_filtered.to_csv(filename.format(th=th), index=False)
    print(f"##### Original data: {len(df)}, Sampled data with {target}: {len(df_filtered)}, th: {th})")
    return df_filtered


if __name__ == "__main__":
    seed = 2024
    random.seed(seed)

    # Load dataset containing average Rouge score and average Cosine-Similarity score
    df_slim_orca, df_kor_open_orca = load_data()

    """
    Filter SlimOrca based on Rouge score 
    """
    # Plot histogram of average Rouge scores
    plot_histogram(data=df_slim_orca['avg_rouge_qarv'],
                   title='SlimOrca with QARV',
                   xlabel='Average Rouge-L',
                   ylabel='Frequency',
                   filename='./output/slim_orca_rouge_histogram.png')
    # Filter SlimOrca based on threshold
    df_slim_orca = filter_dataset(df=df_slim_orca,
                                  target='avg_rouge_qarv',
                                  th=0.1,
                                  filename='./output/slim_orca_rouge_fil_{th}.csv')

    """
    Filter KorOpenOrca based on Rouge score 
    """
    # Plot histogram of average Rouge scores
    plot_histogram(data=df_kor_open_orca['avg_rouge_qarv'],
                   title='KorOpenOrca with QARV',
                   xlabel='Average Rouge-L',
                   ylabel='Frequency',
                   filename='./output/kor_open_orca_rouge_histogram.png')
    # Filter KorOpenOrca based on threshold
    df_kor_open_orca = filter_dataset(df=df_kor_open_orca,
                                      target='avg_rouge_qarv',
                                      th=0.01,
                                      filename='./output/kor_open_orca_rouge_fil_{th}.csv')

    """
    Filter SlimOrca based on Cosine Similarity
    """
    # Plot histogram of average Cosine similarity
    plot_histogram(data=df_slim_orca['avg_cossim_qarv'],
                   title='SlimOrca with QARV',
                   xlabel='Average Cosine Similarity',
                   ylabel='Frequency',
                   filename='./output/slim_orca_cossim_histogram.png')
    # Filter SlimOrca based on threshold
    df_slim_orca = filter_dataset(df=df_slim_orca,
                                  target='avg_cossim_qarv',
                                  th=0.3,
                                  filename='./output/slim_orca_cossim_fil_{th}.csv')

    """
    Filter KorOpenOrca based on Cosine Similarity
    """
    # Plot histogram of average Cosine similarity
    plot_histogram(data=df_kor_open_orca['avg_cossim_qarv'],
                   title='KorOpenOrca with QARV',
                   xlabel='Average Cosine Similarity',
                   ylabel='Frequency',
                   filename='./output/kor_open_orca_cossim_histogram.png')
    # Filter SlimOrca based on threshold
    df_kor_open_orca = filter_dataset(df=df_kor_open_orca,
                                      target='avg_cossim_qarv',
                                      th=0.01,
                                      filename='./output/kor_open_orca_cossim_fil_{th}.csv')

    """
    Equalize the number of samples in SlimOrca and KorOpenOrca
    """
    min_size = min(len(df_slim_orca), len(df_kor_open_orca))
    print(f'##### Min number of samples: {min_size}')
    if len(df_slim_orca) > min_size:
        df_slim_orca = df_slim_orca.sample(n=min_size, random_state=seed)
    elif len(df_kor_open_orca) > min_size:
        df_kor_open_orca = df_kor_open_orca.sample(n=min_size, random_state=seed)

    df_slim_orca.to_csv('./output/slim_orca_fin.csv', index=False)
    df_kor_open_orca.to_csv('./output/kor_open_orca_fin.csv', index=False)
    print(f'##### Final number of samples: SlimOrca - {len(df_slim_orca)}, KorOpenOrca - {len(df_kor_open_orca)}')
