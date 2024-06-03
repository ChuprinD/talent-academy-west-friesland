import mysql.connector
import csv
import os
import subprocess

from src.config import DB_config, Path_to_sql_database


def get_region_id(region_name, region_type, cursor):
    if region_type == 'Gemeente':
        query = "SELECT id FROM gemeente WHERE gemeente_naam = %s"
    elif region_type == 'Corop':
        query = "SELECT id FROM corop WHERE corop_naam = %s"
    else:
        return None
    cursor.execute(query, (region_name,))
    result = cursor.fetchone()
    return result[0] if result else None
    

def update_table(csv_path, table_plan, region_columns):
    try:
        connection = mysql.connector.connect(host=DB_config['host'],
                                             database=DB_config['database'],
                                             user=DB_config['user'],
                                             password=DB_config['password'])

    
        # Firstly clear table
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table_plan['name']}")
        cursor.execute(f"ALTER TABLE {table_plan['name']} AUTO_INCREMENT = 1;")
        connection.commit()
        
        with open(csv_path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)  # Skip the CSV file header

            columns = list(table_plan['columns'].keys())
            # Remove 'id' column for auto-increment
            columns.remove('id')

            # Construct the INSERT SQL query dynamically
            insert_sql = f"INSERT INTO {table_plan['name']} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
             
            # Load data from the CSV file into the table
            for row in csv_reader:
                row_data = []
                for col_name, value in zip(header, row):
                    if col_name in region_columns:
                        region_type_col = 'Niveau regio'
                        region_type = row[header.index(region_type_col)]
                        region_id = get_region_id(value, region_type, cursor) if value else None
                        row_data.append(region_id)
                    else:
                        row_data.append(value)
                cursor.execute(insert_sql, tuple(row_data))
        connection.commit()
        
    except Exception as error:
        print(f"Error connecting to the table: {error}")
    finally:
        cursor.close()
        connection.close()


def dump_database():
    # Form the full path to the dump file
    command = ['mysqldump' , '-u', DB_config['user'], '-p'+DB_config['password'], DB_config['database'], '>', Path_to_sql_database]

    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
