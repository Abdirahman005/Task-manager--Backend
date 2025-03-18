import sqlite3

# Define SQLite database file
db_file = "task_manager_application.db"

def get_connection():
    try:
        # Establish a connection to SQLite
        conn = sqlite3.connect(db_file)
        print("Connected to the SQLite database successfully.")
        return conn
    except Exception as e:
        print("Error while connecting to the database:", e)
        return None

# Test the connection (optional)
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT sqlite_version();")
        record = cursor.fetchone()
        print("SQLite database version:", record[0])
        cursor.close()
        conn.close()
        print("Connection closed.")
