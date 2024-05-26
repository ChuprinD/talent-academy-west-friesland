import pandas as pd
from ..config import (Municipalities, Path_to_raw_data, Path_to_clean_data, COROP)

def clean_young_professionals(name_data_file):
    df = pd.read_csv(Path_to_raw_data + '/' + name_data_file, sep=';')
    
    #Condition for Jaar
    last_year = df['Jaar'].max()
    condition = df['Jaar'] > (last_year - 5)
    df = df[condition] 
    
    #Drop Niveau regio
    df = df.drop('Niveau regio', axis=1) 
    
    #Condition for Regio
    condition = df['Regio'].isin(Municipalities)
    df = df[condition] 
    
    #Condition for Ingeschreven UWV werkbedrijf
    condition = df['Ingeschreven UWV werkbedrijf'] == 'Niet geregistreerd werkzoekende bij UWV'
    df = df[condition]
    df = df.drop('Ingeschreven UWV werkbedrijf', axis=1) 
    
    #Condition for Arbeidspositie
    condition = df['Arbeidspositie'] == 'Werkzame beroepsbevolking'
    df = df[condition] 
    df = df.drop('Arbeidspositie', axis=1) 
    
    #Condition for Onderwijsdeelname
    condition = df['Onderwijsdeelname'] == 'Volgt geen formeel onderwijs'
    df = df[condition] 
    df = df.drop('Onderwijsdeelname', axis=1) 
    
    #Drop Uitkering
    condition = df['Uitkering'] == 'Totaal met of zonder uitkering'
    df = df[condition] 
    df = df.drop('Uitkering', axis=1) 
    
    #Drop Aandeel
    df = df.drop('Aandeel', axis=1)
    
    #Get total number of working in NHN
    sum_by_year = df.groupby('Jaar').agg({'Aantal jongeren': 'sum', 'Totaal aantal jongeren': 'sum'}).reset_index()
    
    total_rows = []
    
    for index, row in sum_by_year.iterrows():
        total_rows.append({'Jaar': row['Jaar'], 'Regio': 'NHN', 'Aantal jongeren': row['Aantal jongeren'],
                            'Totaal aantal jongeren': row['Totaal aantal jongeren']})
    
    total_df = pd.DataFrame(total_rows)
    df = pd.concat([df, total_df])
    
    #Save file
    df.to_csv(Path_to_clean_data + '/' + name_data_file, index=False)


def clean_young_professionals_living_working_region(name_data_file_2018_2020, name_data_file_2021_2022, name_data_file_2018_2022):

    df_2018_2020 = clean_young_professionals_living_working_region_2018_2020(name_data_file_2018_2020)
    df_2021_2022 = clean_young_professionals_living_working_region_2021_2022(name_data_file_2021_2022)

    #Union of two files
    df_2018_2022 = pd.concat([df_2018_2020, df_2021_2022], ignore_index=True)
    df_2018_2022.to_csv(Path_to_clean_data + '/' + name_data_file_2018_2022, index=False)


def clean_young_professionals_living_working_region_2018_2020(name_data_file_2018_2020):
     #clean df_2018_2020
    df_2018_2020 = pd.read_csv(Path_to_raw_data + '/' + name_data_file_2018_2020, sep=';')

    #Condition for Jaar
    last_year = df_2018_2020['Jaar'].max()
    condition = df_2018_2020['Jaar'] > (last_year - 3)
    df_2018_2020 = df_2018_2020[condition] 

    #Drop Niveau regio
    df_2018_2020 = df_2018_2020.drop('Niveau regio', axis=1)

    #Drop Geslacht
    condition = df_2018_2020['Geslacht'] == 'Totaal mannen en vrouwen'
    df_2018_2020 = df_2018_2020[condition]
    df_2018_2020 = df_2018_2020.drop('Geslacht', axis=1)

    #Condition for Woonregio
    condition = df_2018_2020['Woonregio'].isin(COROP)
    df_2018_2020 = df_2018_2020[condition]

    #Condition for Leeftijd
    condition = df_2018_2020['Leeftijd'].isin(['15 tot 20 jaar', '20 tot 25 jaar', '25 tot 30 jaar'])
    df_2018_2020 = df_2018_2020[condition]

    #Drop Woon-werkafstand
    df_2018_2020 = df_2018_2020.drop('Woon-werkafstand', axis=1)

    #Union by age
    df_2018_2020 = df_2018_2020.groupby(['Jaar', 'Woonregio', 'Werkregio']).agg({'Banen': 'sum'}).reset_index()
    df_2018_2020['Leeftijd'] = '15 tot 30 jaar'
    df_2018_2020 = df_2018_2020.drop('Leeftijd', axis=1)
    
    return df_2018_2020


def clean_young_professionals_living_working_region_2021_2022(name_data_file_2021_2022):
        #clean df_2021_2022
    df_2021_2022 = pd.read_csv(Path_to_raw_data + '/' + name_data_file_2021_2022, sep=';')

    #Drop Geslacht
    condition = df_2021_2022['Geslacht'] == 'Totaal mannen en vrouwen'
    df_2021_2022 = df_2021_2022[condition]
    df_2021_2022 = df_2021_2022.drop('Geslacht', axis=1)

    #Drop Leeftijd
    condition = df_2021_2022['Leeftijd'] == '15 tot 30 jaar'
    df_2021_2022 = df_2021_2022[condition]
    df_2021_2022 = df_2021_2022.drop('Leeftijd', axis=1)

    #Condition for Woonregio's
    df_2021_2022['Woonregio\'s'] = df_2021_2022['Woonregio\'s'].str.replace('(CR)', '(C)')
    condition = df_2021_2022['Woonregio\'s'].isin(COROP)
    df_2021_2022 = df_2021_2022[condition]

    #Delete word "december" from Perioden
    df_2021_2022['Perioden'] = df_2021_2022['Perioden'].str.replace('december*', '').str.strip()

    #Multiplying each value by 1000 from Banen van werknemers (x 1 000)
    df_2021_2022['Banen van werknemers (x 1 000)'] = df_2021_2022['Banen van werknemers (x 1 000)'].str.replace(',', '.')
    df_2021_2022['Banen van werknemers (x 1 000)'] = pd.to_numeric(df_2021_2022['Banen van werknemers (x 1 000)'])
    df_2021_2022['Banen van werknemers (x 1 000)'] *= 1000
    df_2021_2022.rename(columns={'Banen van werknemers (x 1 000)': 'Banen_van_werknemers'}, inplace=True)

    #Deleting rows where the value in the 'place of work' column does not end with '(CR)' in Werkregio\'s
    df_2021_2022 = df_2021_2022[df_2021_2022['Werkregio\'s'].str.endswith('(CR)', na=False)]
    df_2021_2022['Werkregio\'s'] = df_2021_2022['Werkregio\'s'].str.replace('(CR)', '(C)')

    #Drop Woon-werkafstand (km)
    df_2021_2022 = df_2021_2022.drop('Woon-werkafstand (km)', axis=1)

    #Change columns position
    df_2021_2022 = df_2021_2022[['Perioden', 'Woonregio\'s', 'Werkregio\'s', 'Banen_van_werknemers']]
    df_2021_2022.rename(columns={'Perioden': 'Jaar',
                                 'Woonregio\'s': 'Woonregio',
                                 'Werkregio\'s': 'Werkregio',
                                 'Banen_van_werknemers': 'Banen'}, inplace=True)
    
    #Save file
    return df_2021_2022