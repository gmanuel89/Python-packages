#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import urllib.parse, requests

## Get list of attributes from tenant
def get_attribute_list(tenant_url: str, tenant_api_key: str, selected_entities=[]) -> list[dict]:
    # Initialise output
    signals_inventa_attribute_list_response_content = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Formulate the URL for API call
    signals_inventa_tenant_api_url_suffix = 'information-design-service/attributes?limit=0'
    # Add possible entities to filter attributes
    if len(selected_entities) > 0:
        signals_inventa_tenant_api_url_suffix = signals_inventa_tenant_api_url_suffix + '&entity='
        for ent in range(len(selected_entities)):
            # Make the string suitable for URL
            signals_inventa_tenant_api_url_suffix = signals_inventa_tenant_api_url_suffix + str(urllib.parse.quote(selected_entities[ent]))
            if ent != len(selected_entities)-1:
                signals_inventa_tenant_api_url_suffix = signals_inventa_tenant_api_url_suffix + ','
    # Retrieve content from tenant
    try:
        signals_inventa_attribute_list_response = requests.get(tenant_url + signals_inventa_tenant_api_url_suffix,
                                                                    headers={'x-api-key': tenant_api_key})
        signals_inventa_attribute_list_response_content = signals_inventa_attribute_list_response.json()
    except:
        signals_inventa_attribute_list_response_content = None
    # return
    return signals_inventa_attribute_list_response_content