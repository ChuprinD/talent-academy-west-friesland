import pandas as pd
from ..config import (Municipalities, Path_to_raw_data, Path_to_clean_data, NHN_COROP, Last_year)


def clean_professionals_living_working_region(name_data_file_2018_2020, name_data_file_2021_2022, name_data_file_2018_2022):
    df_2018_2020 = clean_professionals_living_working_region_2018_2020(name_data_file_2018_2020)
    df_2021_2022 = clean_professionals_living_working_region_2021_2022(name_data_file_2021_2022)

    #Union of two files
    df_2018_2022 = pd.concat([df_2018_2020, df_2021_2022], ignore_index=True)
    df_2018_2022.to_csv(Path_to_clean_data + '/' + name_data_file_2018_2022, index=False)
    

def clean_professionals_living_working_region_2018_2020(name_data_file_2018_2020):
    #clean df_2018_2020
    df_2018_2020 = pd.read_csv(Path_to_raw_data + '/' + name_data_file_2018_2020, sep=';')

    #Condition for Jaar
    last_year = 2020
    condition = df_2018_2020['Jaar'] > (last_year - 3)
    df_2018_2020 = df_2018_2020[condition] 

    #Drop Niveau regio
    #df_2018_2020 = df_2018_2020.drop('Niveau regio', axis=1)

    #Drop Geslacht
    condition = df_2018_2020['Geslacht'] == 'Totaal mannen en vrouwen'
    df_2018_2020 = df_2018_2020[condition]
    df_2018_2020 = df_2018_2020.drop('Geslacht', axis=1)

    #Condition for Woonregio
    condition = df_2018_2020['Woonregio'].isin(NHN_COROP)
    df_2018_2020 = df_2018_2020[condition]

    #Condition for Leeftijd
    condition = df_2018_2020['Leeftijd'].isin(['30 tot 35 jaar', '35 tot 40 jaar', '40 tot 45 jaar', '45 tot 50 jaar', '50 tot 55 jaar', '55 tot 60 jaar', '60 tot 65 jaar', '65 jaar of ouder'])
    df_2018_2020 = df_2018_2020[condition]

    #Drop Woon-werkafstand
    df_2018_2020 = df_2018_2020.drop('Woon-werkafstand', axis=1)

    #Union by age
    df_2018_2020 = df_2018_2020.groupby(['Jaar', 'Niveau regio', 'Woonregio', 'Werkregio']).agg({'Banen': 'sum'}).reset_index()
    df_2018_2020['Leeftijd'] = '30+ jaar'
    df_2018_2020 = df_2018_2020.drop('Leeftijd', axis=1)
    
    return df_2018_2020


def clean_professionals_living_working_region_2021_2022(name_data_file_2021_2022):
    #clean df_2021_2022
    df_2021_2022 = pd.read_csv(Path_to_raw_data + '/' + name_data_file_2021_2022, sep=';')

    #Drop Geslacht
    condition = df_2021_2022['Geslacht'] == 'Totaal mannen en vrouwen'
    df_2021_2022 = df_2021_2022[condition]
    df_2021_2022 = df_2021_2022.drop('Geslacht', axis=1)

    #Drop Leeftijd
    condition = df_2021_2022['Leeftijd'].isin(['30 tot 45 jaar', '45 tot 60 jaar', '60 tot 75 jaar', '75 jaar of ouder'])
    df_2021_2022 = df_2021_2022[condition]

    #Condition for Woonregio's
    df_2021_2022['Woonregio\'s'] = df_2021_2022['Woonregio\'s'].str.replace('(CR)', '(C)')
    condition = df_2021_2022['Woonregio\'s'].isin(NHN_COROP)
    df_2021_2022 = df_2021_2022[condition]

    #Add Niveau regio
    df_2021_2022['Niveau regio'] = 'Corop'

    #Delete word "december" from Perioden
    df_2021_2022['Perioden'] = df_2021_2022['Perioden'].str.replace('december*', '').str.strip()

    #Multiplying each value by 1000 from Banen van werknemers (x 1 000)
    df_2021_2022['Banen van werknemers (x 1 000)'] = df_2021_2022['Banen van werknemers (x 1 000)'].str.replace(',', '.')
    df_2021_2022['Banen van werknemers (x 1 000)'] = pd.to_numeric(df_2021_2022['Banen van werknemers (x 1 000)'])
    df_2021_2022['Banen van werknemers (x 1 000)'] *= 1000
    df_2021_2022.rename(columns={'Banen van werknemers (x 1 000)': 'Banen_van_werknemers'}, inplace=True)

    #Deleting rows where the value in the 'place of work' column does not end with '(CR)' in Werkregio\'s
    condition = df_2021_2022['Werkregio\'s'] != 'Niet in te delen (CR)'
    df_2021_2022 = df_2021_2022[condition]
    df_2021_2022 = df_2021_2022[df_2021_2022['Werkregio\'s'].str.endswith('(CR)', na=False)]
    df_2021_2022['Werkregio\'s'] = df_2021_2022['Werkregio\'s'].str.replace('(CR)', '(C)')

    #Drop Woon-werkafstand (km)
    df_2021_2022 = df_2021_2022.drop('Woon-werkafstand (km)', axis=1)

    #Union by age
    df_2021_2022 = df_2021_2022.groupby(['Perioden', 'Niveau regio', 'Woonregio\'s', 'Werkregio\'s']).agg({'Banen_van_werknemers': 'sum'}).reset_index()
    df_2021_2022['Leeftijd'] = '30+ jaar'
    df_2021_2022 = df_2021_2022.drop('Leeftijd', axis=1)

    #Change columns position
    df_2021_2022 = df_2021_2022[['Perioden', 'Niveau regio', 'Woonregio\'s', 'Werkregio\'s', 'Banen_van_werknemers']]
    df_2021_2022.rename(columns={'Perioden': 'Jaar',
                                 'Woonregio\'s': 'Woonregio',
                                 'Werkregio\'s': 'Werkregio',
                                 'Banen_van_werknemers': 'Banen'}, inplace=True)
    
    return df_2021_2022
