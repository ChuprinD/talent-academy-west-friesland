import pandas as pd
from ..config import (Municipalities, Path_to_raw_data, Path_to_clean_data)

def clean_students(name_data_file):
    df = pd.read_csv(Path_to_raw_data + '/' + name_data_file, sep=';')

    condition = df['Regio'].isin(Municipalities)
    df = df[condition] 

    condition = df['Soort hoger onderwijs'] != 'Totaal'
    df = df[condition]

    condition = df['Opleidingssector'] != 'Totaal'
    df = df[condition]

    test = df['Opleidingssector'].tolist()

    df.to_csv(Path_to_clean_data + '/' + name_data_file, index=False)
