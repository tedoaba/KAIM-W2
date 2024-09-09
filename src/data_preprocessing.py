from sklearn.preprocessing import MinMaxScaler

def aggregate_metrics(df):
    """Aggregates engagement metrics per user."""
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

def normalize_data(agg_data):
    """Normalizes engagement metrics using MinMaxScaler."""
    scaler = MinMaxScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(agg_data), columns=agg_data.columns, index=agg_data.index)
    return normalized_data
