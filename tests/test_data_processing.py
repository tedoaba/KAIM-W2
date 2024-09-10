import pytest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import load_data, describe_data, load_and_preprocess_data

def test_load_data():
    df = load_data('../data/data.csv')
    assert isinstance(df, pd.DataFrame)

def test_describe_data():
    df = load_data('../data/data.csv')
    shape, stats = describe_data(df)
    assert shape == df.shape
    assert 'mean' in stats.columns

def test_load_and_preprocess_data():
    df = load_and_preprocess_data('../data/data.csv')
    assert not df.isnull().values.any()

