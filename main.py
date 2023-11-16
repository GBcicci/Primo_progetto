import pandas as pd
#commit 1 funzione main--> apre il csv con pd
#commit 2 richiama main--> funzione statistica per calcolare qualcosa


if __name__ == '__main__':

    file = pd.read_csv('Airline Delay.csv')
    print(file.head)