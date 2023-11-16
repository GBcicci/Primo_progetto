import pandas as pd
#commit 1 funzione main--> apre il csv con pd
#commit 2 richiama main--> funzione statistica per calcolare qualcosa

def statistica_canciani_savio(df):
    print(df.describe())

def month_frec(df):
    count_year=df.groupby('year').count()
    return count_year

if __name__ == '__main__':
    path = r"Airline Delay.csv"
    df = pd.read_csv(path, sep=',', header=0)
    print(df.head)

    statistica_canciani_savio(df)
    
    



