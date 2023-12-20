import pandas as pd

def index_by_date(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df.set_index('order_date', inplace=True)
    df.sort_index(ascending=False, inplace=True)

def filter_by_date(df, st, en):
    start_date = pd.to_datetime(st)
    end_date = pd.to_datetime(en)
    filtered_df = df.loc[start_date:end_date]

    return filtered_df