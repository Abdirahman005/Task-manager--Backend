mport psycopg2

# Define your connection string
connection_string = "postgresql://pets_adoption_user:OKuq8XY4kZnZjPZqbabjzxI5xLEu640g@dpg-cvbj3ed2ng1s73eejq50-a.oregon-postgres.render.com/pets_adoption"

try:
    # Establish a connection
    conn = psycopg2.connect(connection_string)
    print("Connected to the database successfully.")

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a simple query (optional)
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Database version:", record)

except Exception as e:
    print("Error while connecting to the database:", e)

finally:
    # Close the connection
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed.")