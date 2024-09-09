import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.clustering import perform_clustering

def test_perform_clustering():
    df = pd.read_csv('test_telecom_dataset.csv')
    experience_data = aggregate_experience_data(df)
    experience_data = perform_clustering(experience_data)
    assert 'Experience Cluster' in experience_data.columns
