import pandas as pd

def leggi(csv_path):
    df = pd.read_csv(csv_path, sep=',', header=0)
    print(df.head)
    return df


if __name__ == "__main__":
    path = r"Airline Delay.csv"
    df = leggi(path)
