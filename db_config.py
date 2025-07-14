import mysql.connector
from mysql.connector import Error
import os

def create_connection():
    """
    Create and return a MySQL database connection using environment variables.
    Returns:
        connection (mysql.connector.connection.MySQLConnection): Connection object if successful, else None.
    """
    try:
        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", ""),
            database=os.environ.get("DB_NAME", "grade_db"),
            port=int(os.environ.get("DB_PORT", 3306))
        )
        if connection.is_connected():
            print("✅ Connected to MySQL database")
            return connection
    except Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None

