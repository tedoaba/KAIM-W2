import pytest
import pandas as pd
from src.data_processing import load_and_preprocess_data

def test_load_and_preprocess_data():
    df = load_and_preprocess_data('test_telecom_dataset.csv')
    assert not df.isnull().values.any()
