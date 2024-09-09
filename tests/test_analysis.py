import pandas as pd
from src.analysis import aggregate_experience_data

def test_aggregate_experience_data():
    df = pd.read_csv('test_telecom_dataset.csv')
    experience_data = aggregate_experience_data(df)
    assert 'Avg RTT (ms)' in experience_data.columns
