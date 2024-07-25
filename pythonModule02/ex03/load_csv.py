import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """load data from .csv file"""
    try:
        assert path, "path can't be null"
        assert os.path.exists(path), "path doesn't exist"
        assert len(path) >= 5, "size error"
        assert path[-4:] == ".csv", "only .csv is handled"
    except AssertionError as msg:
        print("AssertionError:", msg)
        raise Exception("")
    pd.options.display.max_rows = 5
    pd.options.display.max_columns = 11
    data = pd.read_csv(path, index_col=False)
    print("Loading dataset of dimensions", data.shape, end="\n\n")
    return data
