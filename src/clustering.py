from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def kmeans_clustering(normalized_data, n_clusters=3):
    """Performs KMeans clustering on normalized data."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(normalized_data)
    labels = kmeans.labels_
    return labels, kmeans

def cluster_statistics(agg_data, labels):
    """Computes cluster statistics for each engagement cluster."""
    agg_data['Engagement Cluster'] = labels
    cluster_stats = agg_data.groupby('Engagement Cluster').agg({
        'Session Duration': ['min', 'max', 'mean', 'sum'],
        'Total Traffic (Bytes)': ['min', 'max', 'mean', 'sum']
    })
    return cluster_stats
