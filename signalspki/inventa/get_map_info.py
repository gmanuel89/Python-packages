#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import requests

## Get the dictionary of a specific Map in Inventa
def get_map_info(tenant_url: str, tenant_api_key: str, selected_map_id='') -> dict:
    # Initialise output
    signals_inventa_map_response_content = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Formulate suffix for API call
    signals_inventa_api_url_suffix = 'information-design-service/import-maps'
    if selected_map_id is not None and selected_map_id != '':
        signals_inventa_api_url_suffix = signals_inventa_api_url_suffix + '/' + selected_map_id
    # Retrieve content from tenant
    try:
        signals_inventa_map_response = requests.get(tenant_url + signals_inventa_api_url_suffix,
                                                                    headers={'x-api-key': tenant_api_key})
        signals_inventa_map_response_content = signals_inventa_map_response.json()
    except:
        signals_inventa_map_response_content = None
    # return
    return signals_inventa_map_response_content
