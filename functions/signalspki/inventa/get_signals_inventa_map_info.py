#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Get the dictionary of a specific Map in Inventa
def get_signals_inventa_map_info(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, selected_map_id='') -> dict:
    # Initialise output
    signals_inventa_map_response_content = []
    # Formulate suffix for API call
    signals_inventa_api_url_suffix = '/information-design-service/import-maps'
    if selected_map_id is not None and selected_map_id != '':
        signals_inventa_api_url_suffix = signals_inventa_api_url_suffix + '/' + selected_map_id
    # Retrieve content from tenant
    signals_inventa_map_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, signals_inventa_api_url_suffix, signals_inventa_tenant_authentication)
    # return
    return signals_inventa_map_response_content
