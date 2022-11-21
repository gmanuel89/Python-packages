#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Get list of maps from tenant
def get_signals_inventa_map_list(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, show_deleted_maps=False, output_type='string') -> list[str] | list[dict]:
    # Initialise output
    map_list = []
    # Generate the suffix for the URL for API call
    tenant_api_url_suffix = '/information-design-service/import-maps?limit=0'
    if show_deleted_maps:
        tenant_api_url_suffix = tenant_api_url_suffix + '&showDeleted=true'
    # Retrieve content from tenant
    signals_inventa_map_list_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication)
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
    # return
    return map_list