#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-01-11
#####

## Import libraries
import requests

## Get list of maps from tenant
def get_map_list(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, show_deleted_maps=False, output_type='string') -> list[str] | list[dict]:
    # Initialise output
    map_list = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Generate the suffix for the URL for API call
    tenant_api_url_suffix = 'information-design-service/import-maps?limit=0'
    if show_deleted_maps:
        tenant_api_url_suffix = tenant_api_url_suffix + '&showDeleted=true'
    # Retrieve content from tenant
    try:
        signals_inventa_map_list_response = requests.get(signals_inventa_tenant_url + tenant_api_url_suffix,
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_map_list_response_content = signals_inventa_map_list_response.json()
        # Retrieve the list of maps
        if str(output_type).lower() == 'string':
            # Add the name of the map to the final list
            for mp in signals_inventa_map_list_response_content:
                map_list.append(mp.get('name'))
        elif str(output_type).lower() == 'dictionary':
            # Add the map to the final list
            for mp in signals_inventa_map_list_response_content:
                map_list.append(mp)
        else:
            pass
    except:
        pass
    # return
    return map_list
