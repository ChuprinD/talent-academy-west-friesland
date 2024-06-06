from src.cleaning.young_professionals import clean_young_professionals, clean_young_professionals_living_working_region
from src.cleaning.professionals import clean_professionals_living_working_region
from src.cleaning.students import clean_students, clean_students_staying_to_work
from src.database_manager import update_table, dump_database
from src.forecasting import forecast_all_professionals, forecast_students
from .config import (Path_to_clean_data, Path_to_forecast_data,
                     Name_young_professionals_data_file, Table_plan_young_professionals,
                     Name_professionals_living_working_region_2018_2020_data_file,
                     Name_professionals_living_working_region_2021_2022_data_file, 
                     Name_young_professionals_living_working_region_2018_2022_data_file, Table_plan_young_professionals_work_live_region,
                     Name_adult_professionals_living_working_region_2018_2022_data_file, Table_plan_adult_professionals_work_live_region,  
                     Name_students_living_region_data_file, Table_plan_students_live_region,
                     Name_students_work_live_region_data_file, Table_plan_students_work_live_region,
                     Name_forecast_young_and_adult_professionals, Table_plan_forecast_professionals,
                     Name_forecast_students, Table_plan_forecast_students)


class App:
    def __init__(self): 
        pass
        
    
    def run(self):
        self.clean_all_data()
        self.create_forecasts()

        self.update_sql_database()
        dump_database()

        
    
    def clean_all_data(self):

        clean_young_professionals(name_data_file=Name_young_professionals_data_file)
        clean_young_professionals_living_working_region(name_data_file_2018_2020=Name_professionals_living_working_region_2018_2020_data_file, 
                                                        name_data_file_2021_2022=Name_professionals_living_working_region_2021_2022_data_file,
                                                        name_data_file_2018_2022=Name_young_professionals_living_working_region_2018_2022_data_file)
        
        clean_professionals_living_working_region(name_data_file_2018_2020=Name_professionals_living_working_region_2018_2020_data_file,
                                                  name_data_file_2021_2022=Name_professionals_living_working_region_2021_2022_data_file,
                                                  name_data_file_2018_2022=Name_adult_professionals_living_working_region_2018_2022_data_file)
        
        clean_students(Name_students_living_region_data_file)  

        clean_students_staying_to_work(Name_students_work_live_region_data_file)

    def update_sql_database(self):
        
        update_table(csv_path=Path_to_clean_data + '/' + Name_young_professionals_data_file,
                     table_plan=Table_plan_young_professionals, region_columns=['Regio'])
        
        update_table(csv_path=Path_to_clean_data + '/' + Name_young_professionals_living_working_region_2018_2022_data_file,
                    table_plan=Table_plan_young_professionals_work_live_region, region_columns=['Woonregio', 'Werkregio'])
        
        update_table(csv_path=Path_to_clean_data + '/' + Name_adult_professionals_living_working_region_2018_2022_data_file,
                    table_plan=Table_plan_adult_professionals_work_live_region, region_columns=['Woonregio', 'Werkregio'])

        update_table(csv_path=Path_to_clean_data + '/' + Name_students_living_region_data_file, table_plan=Table_plan_students_live_region,
                    region_columns=['Regio'], education_type_columns=['Soort hoger onderwijs'], training_sector_columns=['Opleidingssector'])
        
        update_table(csv_path=Path_to_clean_data + '/' + Name_students_work_live_region_data_file,
                     table_plan=Table_plan_students_work_live_region)

        update_table(csv_path=Path_to_forecast_data + '/' + Name_forecast_young_and_adult_professionals,
                     table_plan=Table_plan_forecast_professionals)
        
        update_table(csv_path=Path_to_forecast_data + '/' + Name_forecast_students,
                     table_plan=Table_plan_forecast_students, education_type_columns=['Soort hoger onderwijs'])

    def create_forecasts(self):
        forecast_all_professionals(source_name_young_data_file=Name_young_professionals_living_working_region_2018_2022_data_file,
                                   source_name_adult_data_file=Name_adult_professionals_living_working_region_2018_2022_data_file,
                                   result_name_data_file=Name_forecast_young_and_adult_professionals)
        forecast_students(source_name_data_file=Name_students_living_region_data_file,
                          result_name_data_file=Name_forecast_students)

        

        

        