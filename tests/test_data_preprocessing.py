import pandas as pd
from src.data_processing import load_data, describe_data

def test_load_data():
    df = load_data('data/test_data.csv')
    assert isinstance(df, pd.DataFrame)

def test_describe_data():
    df = load_data('data/test_data.csv')
    shape, stats = describe_data(df)
    assert shape == df.shape
    assert 'mean' in stats.columns
