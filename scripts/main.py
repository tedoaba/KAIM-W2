import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import load_data, describe_data, check_data_quality, aggregate_engagement_metrics
from src.clustering import normalize_data, perform_kmeans_clustering, cluster_statistics
from src.visualization import plot_cluster_boxplots, plot_top_3_applications
from src.analysis import analyze_top_handsets, analyze_top_manufacturers, aggregate_application_data, get_top_10_users_per_application

# Load the dataset
df = load_data('../data/data.csv')

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
