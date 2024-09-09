import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    
    # Fill missing values for numeric columns with mean
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = SimpleImputer(strategy='mean').fit_transform(df[numeric_cols])

    # Fill missing values for categorical columns with the most frequent value
    non_numeric_cols = df.select_dtypes(include=['object']).columns
    df[non_numeric_cols] = df[non_numeric_cols].fillna(df[non_numeric_cols].mode().iloc[0])
    
    return df
