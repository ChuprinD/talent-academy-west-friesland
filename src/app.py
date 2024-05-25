import mysql.connector
from mysql.connector import Error

from src.cleaning.young_professionals import clean_young_professionals
from src.database_manager import update_table, dump_database
from .config import (Municipalities, Path_to_raw_data, Path_to_clean_data,
                        Name_young_professionals_data_file, Table_plan_young_professionals)


class App:
    def __init__(self): 
        pass
        
    
    def run(self):
        self.clean_all_data()
        #self.update_sql_database()
        #dump_database()
    
    def clean_all_data(self):
        
        clean_young_professionals(path_to_raw_data=Path_to_raw_data, path_to_clean_data=Path_to_clean_data,
                                  name_data_file=Name_young_professionals_data_file, municipalities=Municipalities)
        
    def update_sql_database(self):
        update_table(csv_path=Path_to_clean_data + '/' + Name_young_professionals_data_file,
                     table_plan=Table_plan_young_professionals)

        
        