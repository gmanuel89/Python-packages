#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-13
#####

## Import libraries and functions
import requests

## Retrieve the materials library object ID from its name
def get_materials_library_id_from_name(tenant_url: str, tenant_api_key: str, materials_library_name: str) -> str | None:
    ## Initialise output variable
    materials_library_id = None
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Retrieve the response from the tenant through the API
    try:
        tenant_response = requests.get(tenant_url + 'api/rest/v1.0/materials/libraries',
                                        headers={'x-api-key': tenant_api_key})
        tenant_response_content = tenant_response.json()
        for resp in tenant_response_content['data']:
            if resp.get('attributes').get('name') == materials_library_name:
                materials_library_id = resp.get('attributes').get('id')
                break
    except:
        print('Cannot retrieve the list of Materials Libraries from ' + tenant_url)
        pass
    ## return
    return materials_library_id
