import mysql.connector
from mysql.connector import Error

def create_table(db_config, table_name, columns):
    """
    Creates a table in the MySQL database.

    :param db_config: Dictionary with database configuration (host, database, user, password).
    :param table_name: The name of the table to be created.
    :param columns: Dictionary where keys are column names and values are their types.
    """
    try:
        # Connecting to the database
        connection = mysql.connector.connect(
            host=db_config['host'],
            database=db_config['database'],
            user=db_config['user'],
            password=db_config['password']
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Creating a string with column definitions
            columns_str = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
            # Creating the SQL query to create the table
            create_table_query = f"CREATE TABLE {table_name} ({columns_str});"
            cursor.execute(create_table_query)
            connection.commit()
            print(f"Table {table_name} created successfully.")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Example of using the function
db_config = {
    'host': 'localhost',
    'database': 'demographic_data',
    'user': 'root',
    'password': 'your_password'
}

table_name = 'youth_employment'
columns = {
    'year': 'INT NOT NULL',
    'region': 'VARCHAR(100) NOT NULL',
    'number_of_youth': 'INT NOT NULL',
    'number_of_employed_youth': 'INT NOT NULL',
    'PRIMARY KEY': '(year, region)'
}

create_table(db_config, table_name, columns)
