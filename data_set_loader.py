import pandas as pd


def load_dataset(path: str, with_headers = True) -> any:
    file = open(path, "r", encoding='utf-8')

    if with_headers:
        return pd.read_csv(file, sep='\t', encoding='utf-8')
    else:
        return pd.read_csv(file, sep='\t', encoding='utf-8', header = None)

