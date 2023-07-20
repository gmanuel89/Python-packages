#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-22
#####

## Import libraries
import requests

## Determine if a data connection string is an External Connection set up in Inventa
def determine_if_string_is_an_external_connection(data_connection_string: str, tenant_url: str, tenant_api_key: str) -> bool:
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve external connections
    try:
        external_connection_list_response = requests.get(tenant_url + 'information-design-service/external-connections',
                                                        headers={'x-api-key': tenant_api_key})
        external_connection_list_response_content = external_connection_list_response.json()
        # Retrieve the list
        external_connection_list = []
        for resp in external_connection_list_response_content:
            external_connection_list.append(resp.get('name'))
    except:
        external_connection_list = []
    # Determine the match
    return data_connection_string in external_connection_list