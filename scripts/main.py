import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.data_processing import load_and_preprocess_data
from src.analysis import aggregate_experience_data
from src.clustering import perform_clustering

# Load and preprocess data
df = load_and_preprocess_data('../data/data.csv')

# Aggregate experience data
experience_data = aggregate_experience_data(df)

# Perform clustering
experience_data = perform_clustering(experience_data)

print("Aggregated Experience Data Per User:")
print(experience_data.head())
