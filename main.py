import pandas as pd

def open(nome_file):
    percorso_file = f"./{nome_file}"
    dataset = pd.read_csv(percorso_file)
    return dataset

#def stat():
   # return


if __name__ == '__main__':
    nome_file = "Airline Delay.csv"
    dataset_letto = open(nome_file)
    print(dataset_letto.head())