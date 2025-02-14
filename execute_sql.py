import mysql.connector
from mysql.connector import Error
 
DB_CONFIG = {
    'host': 'ankith.mysql.database.azure.com',
    'user': 'ankith',
    'password': 'Admin@1234',
    'database': 'companydb'
}
 
def execute_sql_script(file_path):
    """Executes an SQL script file."""
    connection = None  # Initialize connection variable
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
 
            with open(file_path, 'r') as sql_file:
                sql_script = sql_file.read()
 
            for statement in sql_script.split(';'):
                if statement.strip():
                    cursor.execute(statement)
 
            connection.commit()
            print("SQL script executed successfully.")
 
    except Error as e:
        print(f"Error executing SQL script: {e}")
 
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
 
# Run the script
execute_sql_script('schema_changes.sql')
