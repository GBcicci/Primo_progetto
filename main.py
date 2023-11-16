import pandas as pd

filepath = 'Airline Delay.csv'

def read_file(file_path):
    return  pd.read_csv(file_path)

def statistics(df):
    count_year= df.groupby('year').count()
    return count_year.mean()
