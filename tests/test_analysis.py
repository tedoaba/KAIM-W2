import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analysis import aggregate_experience_data

def test_aggregate_experience_data():
    df = pd.read_csv('../data/data.csv')
    experience_data = aggregate_experience_data(df)
    assert 'Avg RTT (ms)' in experience_data.columns
