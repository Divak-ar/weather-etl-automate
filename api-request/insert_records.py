import psycopg2
from api_request import mock_fetch_data 

def connect_to_db():
    print("Connecting to the database...")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=7000,
            database="db",
            user="divakar",
            password="divakar_password"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

connect_to_db()
