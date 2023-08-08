#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-08-08
#####

## Import libraries
import requests

## Get list of entities from tenant
def get_entity_list(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> list[str]:
    # Initialise output
    entity_list = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content from tenant
    try:
        signals_inventa_entity_list_response = requests.get(signals_inventa_tenant_url + 'information-design-service/entities',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        entity_list = signals_inventa_entity_list_response.json()
    except:
        pass
    # return
    return entity_list