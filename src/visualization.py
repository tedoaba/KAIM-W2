import matplotlib.pyplot as plt
import seaborn as sns

def plot_cluster_boxplots(agg_data):
    """Plot boxplots for session duration and total traffic per cluster."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Engagement Cluster', y='Session Duration', data=agg_data.reset_index())
    plt.title('Session Duration per Engagement Cluster')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Engagement Cluster', y='Total Traffic (Bytes)', data=agg_data.reset_index())
    plt.title('Total Traffic per Engagement Cluster')
    plt.show()

def plot_top_3_applications(app_totals):
    """Plot top 3 most used applications."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Application', y='Total Traffic (Bytes)', data=app_totals)
    plt.title('Top 3 Most Used Applications')
    plt.xlabel('Application')
    plt.ylabel('Total Traffic (Bytes)')
    plt.show()
