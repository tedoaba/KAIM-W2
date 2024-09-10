import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

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

def load_and_preprocess_data(df):
    
    # Separate numeric and non-numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    non_numeric_cols = df.select_dtypes(include=['object']).columns

    # Impute missing numeric values with the mean
    imputer = SimpleImputer(strategy='mean')
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

    # For non-numeric columns, you can fill with the most frequent value (mode) or a custom value
    df[non_numeric_cols] = df[non_numeric_cols].fillna(df[non_numeric_cols].mode().iloc[0])

    # Verify no more missing values
    print(df.isnull().sum())
    
    return df

