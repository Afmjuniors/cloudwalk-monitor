import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Function to establish a connection to the database
def connect_to_database():
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD")
        )
        return conn

    except psycopg2.Error as e:
        # If an error occurs during the connection, print the error message
        print("An error occurred while connecting to the database:", e)
