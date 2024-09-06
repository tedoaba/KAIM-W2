import pytest
from src.data_loader import load_data

def test_load_data():
    path = 'tests/test_data.csv'
    df = load_data(path)
    assert not df.empty
    assert list(df.columns) == ['MSISDN/Number', 'Dur. (ms)', 'Total DL (Bytes)', 'Total UL (Bytes)']
