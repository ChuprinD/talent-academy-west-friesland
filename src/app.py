import mysql.connector
from mysql.connector import Error

from src.cleaning.young_professionals import clean_young_professionals, clean_young_professionals_living_working_region
from src.cleaning.professionals import clean_professionals_living_working_region
from src.database_manager import update_table, dump_database
from .config import (Path_to_clean_data, Name_young_professionals_data_file, Table_plan_young_professionals, Name_professionals_living_working_region_2018_2020_data_file,
                     Name_professionals_living_working_region_2021_2022_data_file, Name_young_professionals_living_working_region_2018_2022_data_file,
                     Name_adult_professionals_living_working_region_2018_2022_data_file, Table_plan_young_professionals_work_live_region,
                     Table_plan_adult_professionals_work_live_region)


class App:
    def __init__(self): 
        pass
        
    
    def run(self):
        self.clean_all_data()
        #self.update_sql_database()
        #dump_database()
    
    def clean_all_data(self):

        clean_young_professionals(name_data_file=Name_young_professionals_data_file)
        clean_young_professionals_living_working_region(name_data_file_2018_2020=Name_professionals_living_working_region_2018_2020_data_file, 
                                                        name_data_file_2021_2022=Name_professionals_living_working_region_2021_2022_data_file,
                                                        name_data_file_2018_2022=Name_young_professionals_living_working_region_2018_2022_data_file)
        
        clean_professionals_living_working_region(name_data_file_2018_2020=Name_professionals_living_working_region_2018_2020_data_file, 
                                                        name_data_file_2021_2022=Name_professionals_living_working_region_2021_2022_data_file,
                                                        name_data_file_2018_2022=Name_adult_professionals_living_working_region_2018_2022_data_file)
        
    def update_sql_database(self):
        
        update_table(csv_path=Path_to_clean_data + '/' + Name_young_professionals_data_file,
                     table_plan=Table_plan_young_professionals, region_columns=['Regio'])
        
        update_table(csv_path=Path_to_clean_data + '/' + Name_young_professionals_living_working_region_2018_2022_data_file,
                    table_plan=Table_plan_young_professionals_work_live_region, region_columns=['Woonregio', 'Werkregio'])
        
        update_table(csv_path=Path_to_clean_data + '/' + Name_adult_professionals_living_working_region_2018_2022_data_file,
                    table_plan=Table_plan_adult_professionals_work_live_region, region_columns=['Woonregio', 'Werkregio'])

        
        