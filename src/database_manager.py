import mysql.connector
import csv
import os
import subprocess

from src.config import DB_config, Path_to_sql_database


def update_table(csv_path, table_plan):
    try:
        connection = mysql.connector.connect(host=DB_config['host'],
                                             database=DB_config['database'],
                                             user=DB_config['user'],
                                             password=DB_config['password'])

    
        # Firstly clear table
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table_plan['name']}")
        connection.commit()
        
        with open(csv_path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the CSV file header

            columns = list(table_plan['columns'].keys())
            # Remove 'id' column for auto-increment
            columns.remove('id')

            # Construct the INSERT SQL query dynamically
            insert_sql = f"INSERT INTO {table_plan['name']} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
             
            # Load data from the CSV file into the table
            for row in csv_reader:
                cursor.execute(insert_sql, tuple(row))  # Exclude 'id' column
        connection.commit()
        
    except Exception as error:
        print(f"Error connecting to the table: {error}")
    finally:
        cursor.close()
        connection.close()
        
#TODO fix this function       
'''        
def dump_database():
    # Form the full path to the dump file
    command = ['mysqldump', '-u', 'root','-p0525','NHN', '>', 'C:/Users/chupr/Desktop/projects/talent-academy-west-friesland/Databases/sql/dump.sql']

    # Запускаем команду в командной строке
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
'''