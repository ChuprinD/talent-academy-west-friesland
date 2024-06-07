import pandas as pd
from ..config import (Municipalities, Path_to_raw_data, Path_to_clean_data)

def clean_students(name_data_file):
    df = pd.read_csv(Path_to_raw_data + '/' + name_data_file, sep=';')

    #Condition for Regio
    condition = df['Regio'].isin(Municipalities)
    df = df[condition] 

    #Condition for Soort hoger onderwijs
    condition = df['Soort hoger onderwijs'] != 'Totaal'
    df = df[condition]

    #Condition for Opleidingssector
    condition = df['Opleidingssector'] != 'Totaal'
    df = df[condition]

    #Renaming of training types 
    df['Opleidingssector'] = df['Opleidingssector'].replace('Gedrag en maatschappij', 'Maatschappijleer')
    df['Opleidingssector'] = df['Opleidingssector'].replace('Landbouw en natuurlijke omgeving', 'Landbouwkunde')
    df['Opleidingssector'] = df['Opleidingssector'].replace('Totaal energietransitie', 'Energietransitie')

    df.to_csv(Path_to_clean_data + '/' + name_data_file, index=False)


def clean_students_staying_to_work(name_data_file):
    df = pd.read_csv(Path_to_raw_data + '/' + name_data_file, sep=';')

    #Drop Niveau regio
    df = df.drop('Niveau regio', axis=1)

    #Drop Woonregio_diploma
    condition = df['Woonregio_diploma'] == 'Noord-Holland Noord (A)'
    df = df[condition]
    df = df.drop('Woonregio_diploma', axis=1)

    #Condition for Werkregio
    condition = df['Werkregio'].isin(['Binnen de regio', 'Buiten de regio'])
    df = df[condition]

    #Drop Onderwijsniveau
    condition = df['Onderwijsniveau'] == 'Totaal'
    df = df[condition]
    df = df.drop('Onderwijsniveau', axis=1)

    #Drop Onderwijsrichting
    condition = df['Onderwijsrichting'] == 'Totaal'
    df = df[condition]
    df = df.drop('Onderwijsrichting', axis=1)

    #Drop Werkend
    condition = df['Werkend'] == 'Ja'
    df = df[condition]
    df = df.drop('Werkend', axis=1)

    #Drop internationaal
    condition = df['internationaal'] == 'Totaal'
    df = df[condition]
    df = df.drop('internationaal', axis=1)

    #Drop Aandeel
    df = df.drop('Aandeel', axis=1)

    #Union by type of peilmoment
    df = df.groupby(['Diplomajaar', 'Werkregio', 'peilmoment']).agg({'Aantal': 'sum'}).reset_index()

    df.to_csv(Path_to_clean_data + '/' + name_data_file, index=False)
