#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Retrieve attributes info
def get_signals_inventa_attribute_info(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: str, selected_attribute_id='') -> dict:
    # Initialise output
    signals_inventa_attribute_response_content = []
    # Formulate the API URL
    signals_inventa_api_url_suffix = '/information-design-service/attributes'
    if selected_attribute_id is not None and selected_attribute_id != '':
        signals_inventa_api_url_suffix = signals_inventa_api_url_suffix + '/' + selected_attribute_id
    # Retrieve content from tenant
    signals_inventa_attribute_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, signals_inventa_api_url_suffix, signals_inventa_tenant_authentication)
    # return
    return signals_inventa_attribute_response_content
