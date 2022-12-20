#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import libraries and functions
import requests

## Get map ID from name
def get_map_id_from_name(signals_inventa_map_name:str, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> str:
    # Initialise output
    map_uid = None
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_map_list_response = requests.get(signals_inventa_tenant_url + 'information-design-service/import-maps?limit=0',
                                                            headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_map_list_response_content = signals_inventa_map_list_response.json()
    except:
        signals_inventa_map_list_response_content = None
    # Get project UID from list
    if signals_inventa_map_list_response_content is not None:
        for mp in signals_inventa_map_list_response_content:
            if str(mp.get('name')).lower() == str(signals_inventa_map_name).lower():
                map_uid = mp.get('_id')
    # return
    return map_uid