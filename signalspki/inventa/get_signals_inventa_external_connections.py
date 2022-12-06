#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import requests

## Retrieve list of External Connections set up in Inventa
def get_signals_inventa_external_connections(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, output_type='text') -> list[str] | list[dict]:
    # Initialise output
    signals_inventa_external_connection_list = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content from tenant
    try:
        signals_inventa_external_connection_list_response = requests.get(signals_inventa_tenant_url + 'information-design-service/external-connections',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_external_connection_list_response_content = signals_inventa_external_connection_list_response.json()
    except:
        signals_inventa_external_connection_list_response_content = None
    # Different outputs
    if signals_inventa_external_connection_list_response_content is not None:
        if str(output_type).lower() == 'text':
            for resp in signals_inventa_external_connection_list_response_content:
                signals_inventa_external_connection_list.append(resp.get('name'))
        else:
            signals_inventa_external_connection_list = signals_inventa_external_connection_list_response_content
    # return
    return signals_inventa_external_connection_list
    
