import pandas as pd

def lettura(path_csv):
    return pd.read_csv(path_csv)

def month_frec(df):
    count_year=df.groupby('year').count()
    return count_year
