#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Retrieve host from a JDBC string
def retrieve_host_from_jdbc_connection(jdbc_connection_string: str) -> str:
    # Initialise output
    host_jdbc = None
    # Split the string to retrieve the type of DB
    jdbc_connection_string_split = jdbc_connection_string.split(':')
    type_of_db = jdbc_connection_string_split[1]
    # PostgreSQL
    if str(type_of_db).lower() == 'postgresql':
        jdbc_connection_host_string = jdbc_connection_string_split[2]
        jdbc_connection_host_string2 = jdbc_connection_host_string.split('/')
        host_jdbc = jdbc_connection_host_string2[len(jdbc_connection_host_string2)-1]
    # Oracle
    elif str(type_of_db).lower() == 'oracle':
        pass
    else:
        pass
    # return
    return host_jdbc