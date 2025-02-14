import mysql.connector
from mysql.connector import Error

# Database configuration (Replace with your actual details)
DB_CONFIG = {
    "host": "ankith.mysql.database.azure.com",  # e.g., "localhost" or Azure MySQL host
    "user": "ankith",                           # Your MySQL username
    "password": "Admin@1234",                   # Your MySQL password
    "database": "companydb"                     # Your database name
}

def execute_sql_script(script_path):
    try:
        # Establish connection to the MySQL database
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print("Successfully connected to the database.")
        
        # Use a cursor to interact with the database
        with conn.cursor() as cursor:
            # Read and split SQL commands from the script
            with open(script_path, 'r') as sql_file:
                sql_commands = sql_file.read().split(";")
                
                # Execute each command in the SQL script
                for command in sql_commands:
                    command = command.strip()
                    if command:
                        print(f"Executing: {command}")
                        cursor.execute(command)
            
            # Commit changes to the database
            conn.commit()
            print("SQL script executed successfully.")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Ensure the connection is closed
        if conn.is_connected():
            conn.close()
            print("Connection closed.")

# Run the script
execute_sql_script("schema_changes.sql")
