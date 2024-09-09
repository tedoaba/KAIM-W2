from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

def perform_clustering(experience_data, n_clusters=3):
    experience_metrics = experience_data[['TCP Retransmission', 'Avg RTT (ms)', 'Avg Throughput (Mbps)']]
    scaler = MinMaxScaler()
    normalized_experience_data = scaler.fit_transform(experience_metrics)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    experience_data['Experience Cluster'] = kmeans.fit_predict(normalized_experience_data)

    return experience_data
