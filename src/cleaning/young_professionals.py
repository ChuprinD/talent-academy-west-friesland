import pandas as pd

def clean_young_professionals(path_to_raw_data, path_to_clean_data, name_data_file, municipalities):
    df = pd.read_csv(path_to_raw_data + '/' + name_data_file, sep=';')
    
    #Condition for Jaar
    last_year = df['Jaar'].max()
    condition = df['Jaar'] > (last_year - 5)
    df = df[condition] 
    
    #Drop Niveau regio
    df = df.drop('Niveau regio', axis=1) 
    
    #Condition for Regio
    condition = df['Regio'].isin(municipalities)
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
    df.to_csv(path_to_clean_data + '/' + name_data_file, index=False)