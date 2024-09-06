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
    
    # Plot cluster results
    plot_cluster_results(agg_data, 'Session Duration')
    plot_cluster_results(agg_data, 'Total Traffic (Bytes)')
    
if __name__ == "__main__":
    data_path = "../data/data.csv"
    main(data_path)
