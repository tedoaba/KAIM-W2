import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import load_data, describe_data, check_data_quality, aggregate_engagement_metrics
from src.clustering import normalize_data, perform_kmeans_clustering, cluster_statistics
from src.visualization import plot_cluster_boxplots, plot_top_3_applications
from src.analysis import analyze_top_handsets, analyze_top_manufacturers, aggregate_application_data, get_top_10_users_per_application
from src.data_loader import load_data
from src.data_preprocessing import aggregate_metrics, normalize_data
from src.clustering import kmeans_clustering, cluster_statistics
from src.visualization import plot_cluster_results, plot_top_app_usage

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
    
if __name__ == "__main__":
    data_path = "../data/data.csv"
    main(data_path)