
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def normalize_data(agg_data):
    """Normalize engagement metrics using MinMaxScaler."""
    scaler = MinMaxScaler()
    return pd.DataFrame(scaler.fit_transform(agg_data), columns=agg_data.columns, index=agg_data.index)

def perform_kmeans_clustering(data, n_clusters=3):
    """Apply K-Means clustering to engagement data."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    return kmeans.labels_

def cluster_statistics(agg_data):
    """Return statistics for each cluster."""
    return agg_data.groupby('Engagement Cluster').agg({
        'Session Duration': ['min', 'max', 'mean', 'sum'],
        'Total Traffic (Bytes)': ['min', 'max', 'mean', 'sum']
    })

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

