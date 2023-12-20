import pandas as pd

def replace_mean(df):
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    mean_value = df['amount'].mean(skipna=True)
    df['amount'].fillna(mean_value, inplace=True)

def fill_gap_forward(df):
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['amount'].fillna(method='ffill', inplace=True)

def drop_row(df):
    df.dropna(subset=['amount'], inplace=True)