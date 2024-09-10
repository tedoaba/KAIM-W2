import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

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
