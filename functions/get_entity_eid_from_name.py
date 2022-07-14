## Import libraries and functions
import requests
from functions.formulate_headers_for_tenant_call import *

## Retrieve the entoty object EID from its name
def get_entity_eid_from_name(tenant_url: str, tenant_authentication: dict, entity_type: str, entity_name: str):
    ## Initialise output variable
    entity_eid = None
    # Formulate headers
    headers_api_call = formulate_headers_for_tenant_call(tenant_authentication.get('authentication_type'), tenant_authentication.get('authentication_parameters'))
    ## Materials library
    if 'material' in entity_type:
        # Formulate the API URL
        tenant_api_url = tenant_url + '/api/rest/v1.0/materials/libraries'
        # Retrieve the response from the tenant through the API
        try:
            tenant_response = requests.get(tenant_api_url, headers=headers_api_call)
            if tenant_response.ok:
                tenant_response_content = tenant_response.json()
                for resp in tenant_response_content['data']:
                    if resp.get('attributes').get('name') == entity_name:
                        entity_eid = resp.get('attributes').get('id')
                        break
        except:
            print('Cannot retrieve the list of Materials Libraries from ' + tenant_url)
            pass
    ## Grids (Tables and ADTs)
    elif 'grid' in entity_type or 'table' in entity_type:
        # Formulate the API URL
        tenant_api_url = tenant_url + '/api/rest/v1.0/entities?includeTypes=grid&page[limit]=100'
        # Retrieve the response from the tenant through the API
        try:
            tenant_response = requests.get(tenant_api_url, headers=headers_api_call)
            if tenant_response.ok:
                tenant_response_content = tenant_response.json()
                for resp in tenant_response_content['data']:
                    if resp.get('attributes').get('name') == entity_name:
                        entity_eid = resp.get('attributes').get('eid')
                        break
        except:
            print('Cannot retrieve the list of Tables from ' + tenant_url)
            pass
    ## Others
    else:
        pass
    ## return
    return entity_eid