#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import requests

## Retrieve attributes info
def get_signals_inventa_attribute_info(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, selected_attribute_id='') -> dict:
    # Initialise output
    signals_inventa_attribute_response_content = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Formulate the API URL
    signals_inventa_api_url_suffix = 'information-design-service/attributes'
    if selected_attribute_id is not None and selected_attribute_id != '':
        signals_inventa_api_url_suffix = signals_inventa_api_url_suffix + '/' + selected_attribute_id
    # Retrieve content from tenant
    try:
        signals_inventa_attribute_response = requests.get(signals_inventa_tenant_url + signals_inventa_api_url_suffix,
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_attribute_response_content = signals_inventa_attribute_response.json()
    except:
        signals_inventa_attribute_response_content = None
    # return
    return signals_inventa_attribute_response_content
