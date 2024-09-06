import seaborn as sns
import matplotlib.pyplot as plt

def plot_cluster_results(agg_data, metric, cluster_label='Engagement Cluster'):
    """Generates a boxplot for clusters."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=cluster_label, y=metric, data=agg_data.reset_index())
    plt.title(f'{metric} per {cluster_label}')
    plt.show()

def plot_top_app_usage(app_totals):
    """Generates a bar plot for top application usage."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Application', y='Total Traffic (Bytes)', data=app_totals)
    plt.title('Top 3 Most Used Applications')
    plt.show()
