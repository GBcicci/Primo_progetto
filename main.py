import pandas as pd
#commit 1 funzione main--> apre il csv con pd
#commit 2 richiama main--> funzione statistica per calcolare qualcosa

if __name__ == '__main__':
    path = r"Airline Delay.csv"
    df = pd.read_csv(path, sep=',', header=0)
    print(df.head)

