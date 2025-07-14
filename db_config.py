import mysql.connector
from mysql.connector import Error
import os

def create_connection():
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

# Example usage:
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in database:")
        for table in tables:
            print("-", table[0])
        cursor.close()
        conn.close()
import mysql.connector
from mysql.connector import Error
import os

def create_connection():
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
