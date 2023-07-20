#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-07-17
#####

## Import libraries
import requests

## Creates a new Inventa map
def create_new_map(map_json: str, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    map_creation_tenant_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Trigger the map creation
    try:
        map_creation_tenant_response = requests.post(tenant_url + 'information-design-service/import-maps',
                                                            headers={'x-api-key': tenant_api_key},
                                                            data=map_json
                                                            )
    except:
        pass
    # return
    return map_creation_tenant_response
