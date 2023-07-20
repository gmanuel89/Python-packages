#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-10-07
#####

## Retrieve database from a JDBC string
def retrieve_database_from_jdbc_connection(jdbc_connection_string: str) -> str:
    # Initialise output
    database_jdbc = None
    # Split the string to retrieve the type of DB
    jdbc_connection_string_split = jdbc_connection_string.split(':')
    type_of_db = jdbc_connection_string_split[1]
    # PostgreSQL
    if str(type_of_db).lower() == 'postgresql':
        jdbc_connection_string_split = jdbc_connection_string.split('/')
        database_jdbc = jdbc_connection_string_split[len(jdbc_connection_string_split)-1]
    # Oracle
    elif str(type_of_db).lower() == 'oracle':
        pass
    else:
        pass
    # return
    return database_jdbc