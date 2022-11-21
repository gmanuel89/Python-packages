#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Get list of attributes from tenant
def get_signals_inventa_attribute_list(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, selected_entities=[]) -> dict:
    # Initialise output
    signals_inventa_attribute_list_response_content = []
    # Formulate the URL for API call
    signals_inventa_tenant_api_url_suffix = '/information-design-service/attributes?limit=0'
    # Add possible entities to filter attributes
    if len(selected_entities) > 0:
        signals_inventa_tenant_api_url_suffix = signals_inventa_tenant_api_url_suffix + '&entity='
        for ent in range(len(selected_entities)):
            signals_inventa_tenant_api_url_suffix = signals_inventa_tenant_api_url_suffix + str(selected_entities[ent])
            if ent != len(selected_entities)-1:
                signals_inventa_tenant_api_url_suffix = signals_inventa_tenant_api_url_suffix + ','
    # Retrieve content from tenant
    signals_inventa_attribute_list_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, signals_inventa_tenant_api_url_suffix, signals_inventa_tenant_authentication)
    # return
    return signals_inventa_attribute_list_response_content