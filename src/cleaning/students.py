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

    condition = df['Regio'].isin(Municipalities)
    df = df[condition] 

    df.to_csv(Path_to_clean_data + '/' + name_data_file, index=False)


def clean_students_staying_to_work(name_data_file):
    df = pd.read_csv(Path_to_raw_data + '/' + name_data_file, sep=';')

    df = df.drop('Niveau regio', axis=1)

    condition = df['Woonregio_diploma'] == 'Noord-Holland Noord (A)'
    df = df[condition]
    df = df.drop('Woonregio_diploma', axis=1)

    condition = df['Werkregio'].isin(['Binnen de regio', 'Buiten de regio'])
    df = df[condition]

    condition = df['Onderwijsniveau'] == 'Totaal'
    df = df[condition]
    df = df.drop('Onderwijsniveau', axis=1)

    condition = df['Onderwijsrichting'] == 'Totaal'
    df = df[condition]
    df = df.drop('Onderwijsrichting', axis=1)

    condition = df['Werkend'] == 'Ja'
    df = df[condition]
    df = df.drop('Werkend', axis=1)

    condition = df['internationaal'] == 'Totaal'
    df = df[condition]
    df = df.drop('internationaal', axis=1)

    df = df.drop('Aandeel', axis=1)

    df = df.groupby(['Diplomajaar', 'Werkregio', 'peilmoment']).agg({'Aantal': 'sum'}).reset_index()

    df.to_csv(Path_to_clean_data + '/' + name_data_file, index=False)
