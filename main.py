import pandas as pd
#commit 1 funzione main--> apre il csv con pd
#commit 2 richiama main--> funzione statistica per calcolare qualcosa


if __name__ == '__main__':

    file = pd.read_csv('Airline Delay.csv')
    #print(dataset.head)


    def analyze_dataset(dataset):
        total_flights = dataset['arr_flights'].sum()
        return total_flights

    print(analyze_dataset(file))