import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Fetch database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def execute_sql_file(file_path):
    """
    Executes a .sql file to set up database schema and tables.

    :param file_path: Path to the .sql file.
    """
    try:
        # Connect to the existing database
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()

        # Open and execute the SQL file
        with open(file_path, 'r') as file:
            sql_content = file.read()
            cursor.execute(sql_content)
            connection.commit()
            print(f"SQL file {file_path} executed successfully")

        # Close the connection
        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error while executing SQL file: {e}")

def load_data_from_postgres(query):
    """
    Connects to the PostgreSQL database and loads data based on the provided SQL query.

    :param query: SQL query to execute.
    :return: DataFrame containing the results of the query.
    """
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        # Load data using pandas
        df = pd.read_sql_query(query, connection)

        # Close the database connection
        connection.close()

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def load_data_using_sqlalchemy(query):
    """
    Connects to the PostgreSQL database and loads data based on the provided SQL query using SQLAlchemy.

    :param query: SQL query to execute.
    :return: DataFrame containing the results of the query.
    """
    try:
        # Create a connection string
        connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

        # Create an SQLAlchemy engine
        engine = create_engine(connection_string)

        # Load data into a pandas DataFrame
        df = pd.read_sql_query(query, engine)

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main code
if __name__ == "__main__":
    # Step 1: Execute the SQL file to set up schema/tables
    #sql_file_path1 = "../schema.sql"
    sql_file_path2 = "../telecom.sql"
    #execute_sql_file(sql_file_path1)
    execute_sql_file(sql_file_path2)

    # Step 2: Example usage of load data
    #sample_query = "SELECT * FROM xdr_data"
    #df = load_data_using_sqlalchemy(sample_query)
    #if df is not None:
       # print(df.head())
