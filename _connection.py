import psycopg2

connection_string = "dbname='task_manager_application' user='task_manager_application_user' password='RUvV3gmQa4QPhw35XKMX0suNQWSB0xfl' host='dpg-cvbr5st2ng1s73eh1530-a.oregon-postgres.render.com' port='5432'"

try:
    conn = psycopg2.connect(connection_string)
    print("Connected to the database successfully.")

    cursor = conn.cursor()

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Database version:", record)

except Exception as e:
    print("Error while connecting to the database:", e)

finally:
    if 'conn' in locals() and conn is not None:
        cursor.close()
        conn.close()
        print("Connection closed.")
