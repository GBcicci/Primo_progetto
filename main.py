import pandas as pd
#commit 1 funzione main--> apre il csv con pd
#commit 2 richiama main--> funzione statistica per calcolare qualcosa

def statistica_canciani_savio(df):
    print(df.describe())

if __name__ == '__main__':
    path = r"Airline Delay.csv"
    df = pd.read_csv(path, sep=',', header=0)
    print(df.head)

    statistica_canciani_savio(df)

def statistiche(data_str):

    df = pd.read_csv(StringIO(data_str), sep='\t')

    colonne_utilizzate = ['arr_flights', 'arr_del15', 'arr_delay', 'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay']
    statistiche = df[colonne_utilizzate].agg(['mean', 'max'])
    return statistiche

risultato_statistiche = statistiche(data_str)
print(risultato_statistiche)
