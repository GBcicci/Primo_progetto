import pandas as pd
#commit 1 funzione main--> apre il csv con pd
#commit 2 richiama main--> funzione statistica per calcolare qualcosa

def leggi(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def month_frec(df):
    count_year=df.groupby('year').count()
    return count_year

def statistica(df: pd.DataFrame) -> str:
    # media ritardi sull aeroporto di Birminghan nel 2020
    df_filtered = df[(df['airport'] == 'BHM') & (df['year'] == 2020)]
    avg_dealy = df_filtered['arr_delay'].mean()
    print(f"media ritardi:{avg_dealy}")


if __name__ == '__main__':
    path = r"C:\Users\GiuseppeBase\PycharmProjects\MachineLearning\Data_lake\Airline Delay.csv"
    statistica(leggi(path))

