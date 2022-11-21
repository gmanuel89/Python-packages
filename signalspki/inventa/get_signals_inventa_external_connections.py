#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Retrieve list of External Connections set up in Inventa
def get_signals_inventa_external_connections(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, output_type='text') -> list[str] | list[dict]:
    # Initialise output
    signals_inventa_external_connection_list = []
    # Get response from the tenant
    # Formulate the URL for API call
    signals_inventa_tenant_api_url_suffix = '/information-design-service/external-connections'
    # Retrieve content from tenant
    signals_inventa_external_connection_list_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, signals_inventa_tenant_api_url_suffix, signals_inventa_tenant_authentication)
    # Different outputs
    if str(output_type).lower() == 'text':
        for resp in signals_inventa_external_connection_list_response_content:
            signals_inventa_external_connection_list.append(resp.get('name'))
    else:
        signals_inventa_external_connection_list = signals_inventa_external_connection_list_response_content
    # return
    return signals_inventa_external_connection_list
    
