#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-21
#####

## Import libraries
import requests

## Get map ID from name
def get_map_id_from_name(map_name: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output
    map_id = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content
    try:
        map_list_response = requests.get(tenant_url + 'information-design-service/import-maps?limit=0',
                                        headers={'x-api-key': tenant_api_key})
        map_list_response_content = map_list_response.json()
        # Get map UID from list
        for mp in map_list_response_content:
            if str(mp.get('name')).lower() == str(map_name).lower():
                map_id = mp.get('_id')
    except:
        pass
    # return
    return map_id