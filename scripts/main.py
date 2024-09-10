import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.append(os.path.abspath('../src'))

import pandas as pd
from data_processing import load_and_preprocess_data
from analysis import aggregate_experience_data
from clustering import perform_clustering

from load_data import load_data_from_postgres, load_data_using_sqlalchemy

# Define your SQL query
query = "SELECT * FROM xdr_data;"  # Replace with your actual table name

# Load data from PostgreSQL
df = load_data_from_postgres(query)

# Display the first few rows of the dataframe
if df is not None:
    print("Successfully loaded the data")
else:
    print("Failed to load data.")

# Load and preprocess data
df = load_and_preprocess_data(df)
df.head()

# Aggregate experience data
experience_data = aggregate_experience_data(df)
experience_data.head()

# Perform clustering
experience_data = perform_clustering(experience_data)

print("Aggregated Experience Data Per User:")
print(experience_data.head())
