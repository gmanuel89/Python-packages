#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-07-17
#####

## Import libraries
import requests

## Get map ID from name
def get_map_id_from_name(map_name: str, tenant_url: str, tenant_api_key: str, map_version=None) -> str:
    # Initialise output
    map_id = None
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Retrieve content
    try:
        map_list_response = requests.get(tenant_url + 'information-design-service/import-maps?limit=0&showDeleted=true',
                                        headers={'x-api-key': tenant_api_key})
        map_list_response_content = map_list_response.json()
        # Get map UID from list
        for mp in map_list_response_content:
            if str(mp.get('name')) == str(map_name):
                if map_version is not None and map_version != 0:
                    if mp.get('version') == map_version:
                        map_id = mp.get('_id')
                        break
                    else:
                        map_id = mp.get('_id') # retrieve the latest map if no matching version is found
                else:
                    map_id = mp.get('_id')
    except:
        pass
    # return
    return map_id