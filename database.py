import psycopg2
from flask import Flask, request, render_template

app = Flask(__name__)

# Route for rendering the form
@app.route('/')
def index():
    return render_template('index.html')

# Route for form submission
@app.route('/save_form', methods=['POST'])
def save_form():
    # Retrieve the form data
    name = request.form['name']
    age = int(request.form['age'])
    county = request.form['county']
    year = int(request.form['year'])

    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host='localhost',
        database='DYS_student',
        user='postgres',
        password='Guitar04'
    )

    try:
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute the SQL query to insert form data
        cursor.execute(
            'INSERT INTO form_data (name, age, county, year_of_commitment) VALUES (%s, %s, %s, %s)',
            (name, age, county, year)
        )

        # Commit the changes to the database
        conn.commit()

        return 'Form data saved successfully!'
    except (Exception, psycopg2.Error) as error:
        print('Error: ', error)
        return 'An error occurred while saving form data.'
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run()
