#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and function
import psycopg2
import pandas as pd
from functions.database_handling.retrieve_host_from_jdbc_connection import retrieve_host_from_jdbc_connection
from functions.database_handling.retrieve_database_from_jdbc_connection import retrieve_database_from_jdbc_connection
from functions.csv_handling.convert_csv_content import convert_csv_content

## Read tabular data from DB
def read_data_from_database(jdbc_connection_string, sql_username, sql_password, sql_query, output_type='dictionary') -> list[list] | list[dict]:
    # Initialise output
    table_data = []
    # Retrieve connection parameters from the JDBC connection
    db_host = retrieve_host_from_jdbc_connection(jdbc_connection_string)
    db_database = retrieve_database_from_jdbc_connection(jdbc_connection_string)
    # Establish the connection with the DB
    db_connector = psycopg2.connect(
    host=db_host,
    database=db_database,
    user=sql_username,
    password=sql_password)
    # Read the table as a pandas DataFrame
    db_table_data_frame = pd.read_sql_query(sql=sql_query, con=db_connector)
    # Convert to dictionary or list of lists
    table_data = db_table_data_frame.to_dict(orient='records')
    if str(output_type).lower() == 'list':
        table_data = convert_csv_content(table_data)
    # return
    return table_data