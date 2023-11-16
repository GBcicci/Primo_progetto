import pandas as pd
#commit 1 funzione main--> apre il csv con pd
#commit 2 richiama main--> funzione statistica per calcolare qualcosa
def leggi(path:str)->pd.DataFrame:
    return pd.read_csv(path)


if __name__ == '__main__':
    path=r"C:\Users\GiuseppeBase\PycharmProjects\MachineLearning\Data_lake\Airline Delay.csv"
    df=leggi(path)
    print(df)