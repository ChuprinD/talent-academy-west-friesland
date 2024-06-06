import pandas as pd
from src.config import Path_to_clean_data, Path_to_forecast_data, NHN_COROP

def calcualte_moving_average(df, forecast_column_name):
    window_size = 3
    number_years_forecast = 5

    for i in range(1, number_years_forecast + 1):
        moving_average = df[forecast_column_name].rolling(window=window_size).mean()

        forecast_2023 = int(moving_average.iloc[-1])

        if 'Schooljaar' in df.columns:
            next_year = str(2022 + i) + '/' + str(2022 + i + 1)
        else:
            next_year = 2022 + i
            
        df.loc[ len(df.index )] = [next_year, forecast_2023]

    return df


def forecast_all_professionals(source_name_young_data_file, source_name_adult_data_file, result_name_data_file):
    df_young = forecast_professionals(source_name_young_data_file)
    df_young['Leeftijd'] = 'Jonge'
    df_adult = forecast_professionals(source_name_adult_data_file)
    df_adult['Leeftijd'] = 'Volwassen'

    df = pd.concat([df_young, df_adult], ignore_index=True)
    df.to_csv(Path_to_forecast_data + '/' + result_name_data_file, index=False)


def forecast_professionals(name_data_file):
    df_work_in_NHN = pd.read_csv(Path_to_clean_data + '/' + name_data_file, sep=',')

    condition = df_work_in_NHN['Werkregio'].isin(NHN_COROP)
    df_work_in_NHN = df_work_in_NHN[condition]
    df_work_in_NHN = df_work_in_NHN.groupby(['Jaar']).agg({'Banen': 'sum'}).reset_index()
    
    df_work_in_NHN = calcualte_moving_average(df_work_in_NHN, 'Banen')
    df_work_in_NHN['Werk in NHN'] = 'Ja'


    df_work_out_NHN = pd.read_csv(Path_to_clean_data + '/' + name_data_file, sep=',')

    condition = ~df_work_out_NHN['Werkregio'].isin(NHN_COROP)
    df_work_out_NHN = df_work_out_NHN[condition]
    df_work_out_NHN = df_work_out_NHN.groupby(['Jaar']).agg({'Banen': 'sum'}).reset_index()
    
    df_work_out_NHN = calcualte_moving_average(df_work_out_NHN, 'Banen')
    df_work_out_NHN['Werk in NHN'] = 'Geen'


    df = pd.concat([df_work_in_NHN, df_work_out_NHN], ignore_index=True)
    return df


def forecast_students(source_name_data_file, result_name_data_file):
    df_hbo = pd.read_csv(Path_to_clean_data + '/' + source_name_data_file, sep=',')

    condition = df_hbo['Soort hoger onderwijs'] == 'HBO'
    df_hbo = df_hbo[condition]
    df_hbo = df_hbo.groupby(['Schooljaar']).agg({'Aantal': 'sum'}).reset_index()

    df_hbo = calcualte_moving_average(df_hbo, 'Aantal')
    df_hbo['Soort hoger onderwijs'] = 'HBO'


    df_wo = pd.read_csv(Path_to_clean_data + '/' + source_name_data_file, sep=',')

    condition = df_wo['Soort hoger onderwijs'] == 'WO'
    df_wo = df_wo[condition]
    df_wo = df_wo.groupby(['Schooljaar']).agg({'Aantal': 'sum'}).reset_index()

    df_wo = calcualte_moving_average(df_wo, 'Aantal')
    df_wo['Soort hoger onderwijs'] = 'WO'


    df = pd.concat([df_hbo, df_wo], ignore_index=True)
    df.to_csv(Path_to_forecast_data + '/' + result_name_data_file, index=False)
    
    
