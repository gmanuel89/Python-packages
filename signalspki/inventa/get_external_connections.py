#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import requests

## Retrieve list of External Connections set up in Inventa
def get_external_connections(tenant_url: str, tenant_api_key: str, output_type='text') -> list[str] | list[dict]:
    # Initialise output
    external_connection_list = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content from tenant
    try:
        external_connection_list_response = requests.get(tenant_url + 'information-design-service/external-connections',
                                                                    headers={'x-api-key': tenant_api_key})
        external_connection_list_response_content = external_connection_list_response.json()
    except:
        external_connection_list_response_content = None
    # Different outputs
    if external_connection_list_response_content is not None:
        if str(output_type).lower() == 'text':
            for resp in external_connection_list_response_content:
                external_connection_list.append(resp.get('name'))
        else:
            external_connection_list = external_connection_list_response_content
    # return
    return external_connection_list
    
