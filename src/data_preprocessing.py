import pandas as pd

def load_data(path):
    """Load dataset from a CSV file."""
    return pd.read_csv(path)

def describe_data(df):
    """Return data shape and statistics."""
    return df.shape, df.describe()

def check_data_quality(df):
    """Check for missing and duplicate values."""
    missing_values = df.isnull().sum()
    duplicates = df.duplicated().sum()
    return missing_values, duplicates

def aggregate_engagement_metrics(df):
    """Aggregate customer engagement metrics."""
    agg_data = df.groupby('MSISDN/Number').agg({
        'Dur. (ms)': 'sum',
        'Total DL (Bytes)': 'sum',
        'Total UL (Bytes)': 'sum'
    }).rename(columns={
        'Dur. (ms)': 'Session Duration',
        'Total DL (Bytes)': 'Total DL (Bytes)',
        'Total UL (Bytes)': 'Total UL (Bytes)'
    })
    agg_data['Total Traffic (Bytes)'] = agg_data['Total DL (Bytes)'] + agg_data['Total UL (Bytes)']
    return agg_data
