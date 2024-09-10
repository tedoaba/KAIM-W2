import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#sys.path.append(os.path.abspath('../src'))

from src.data_processing import load_data, describe_data, check_data_quality, aggregate_engagement_metrics
from src.clustering import normalize_data, perform_kmeans_clustering, cluster_statistics
from src.visualization import plot_cluster_boxplots, plot_top_3_applications
from src.analysis import analyze_top_handsets, analyze_top_manufacturers, aggregate_application_data, get_top_10_users_per_application
from src.data_loader import load_data
from src.data_preprocessing import aggregate_metrics, normalize_data
from src.clustering import kmeans_clustering, cluster_statistics
from src.visualization import plot_cluster_results, plot_top_app_usage

import pandas as pd
from data_processing import load_and_preprocess_data
from analysis import aggregate_experience_data
from clustering import perform_clustering

from src.load_data import load_data_from_postgres, load_data_using_sqlalchemy

def main(path):
    # Load the dataset
    df = load_data(path)
    
    # Aggregate metrics per user
    agg_data = aggregate_metrics(df)
    
    # Normalize the engagement data
    normalized_data = normalize_data(agg_data)
    
    # Perform KMeans clustering
    labels, _ = kmeans_clustering(normalized_data, n_clusters=3)
    
    # Compute cluster statistics
    stats = cluster_statistics(agg_data, labels)
    print(stats)

    # Data description
    shape, stats = describe_data(df)
    print(f"Data shape: {shape}")
    print(f"Data statistics: \n{stats}")

    # Check for missing and duplicate data
    missing_values, duplicates = check_data_quality(df)
    print(f"Missing values:\n{missing_values}\n")
    print(f"Duplicate rows: {duplicates}")

    # Perform aggregation and clustering
    agg_data = aggregate_engagement_metrics(df)
    normalized_data = normalize_data(agg_data)
    agg_data['Engagement Cluster'] = perform_kmeans_clustering(normalized_data)
    print(cluster_statistics(agg_data))

    # Visualizations
    plot_cluster_boxplots(agg_data)
    # Plot cluster results
    plot_cluster_results(agg_data, 'Session Duration')
    plot_cluster_results(agg_data, 'Total Traffic (Bytes)')
    

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
    
if __name__ == "__main__":
    data_path = "../data/data.csv"
    main(data_path)
