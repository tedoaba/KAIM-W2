import pytest
from src.data_loader import load_data

def test_load_data():
    path = '../data/data.csv'
    df = load_data(path)
    assert not df.empty