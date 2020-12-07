import pandas as pd


def load_dataset(path: str) -> any:
    file = open(path, "r", encoding='utf-8')
    return pd.read_csv(file, sep='\t', encoding='utf-8')
