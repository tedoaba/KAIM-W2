import pandas as pd

def load_data(path):
    """Loads the telecom dataset from a CSV file."""
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        raise ValueError(f"Error loading data: {e}")
