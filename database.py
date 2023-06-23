import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    port = "5432",
    database = "DYS_student",
    user = "postgres",
    password= "Guitar04"
)