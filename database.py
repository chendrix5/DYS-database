import psycopg2


    # Establish connection
conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="DYS_student",
        user="postgres",
        password="Guitar04"
    )


# Create a cursor object
cursor = conn.cursor()

# Execute SQL query to create the table
query = """
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(255)
)
"""
cursor.execute(query)

# Commit the transaction (if necessary)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
