#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.inventa.get_external_connections import get_external_connections

## Determine if a data connection string is an External Connection set up in Inventa
def determine_if_string_is_an_external_connection(data_connection_string: str, tenant_url: str, tenant_api_key: str) -> bool:
    # Retrieve external connections
    signals_inventa_external_connections = get_external_connections(tenant_url, tenant_api_key, 'text')
    # Determine the match
    return data_connection_string in signals_inventa_external_connections