import mysql.connector
from mysql.connector import Error

# Database configuration (Replace with your actual details)
DB_CONFIG = {
    "host": "ankith.mysql.database.azure.com",  # e.g., "localhost" or Azure MySQL host
    "user": "ankith",
    "password": "Admin@1234",
    "database": "companydb"
}

def execute_sql_script(script_path):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Read and execute SQL script
        with open(script_path, 'r') as sql_file:
            sql_commands = sql_file.read().split(";")
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)
        
        # Commit changes
        conn.commit()
        print("SQL script executed successfully.")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Run the script
execute_sql_script("schema_changes.sql")
