#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-14
#####

## Import libraries and functions
import requests

## Get the Link entry from the entity retrieval response
def get_link_entry_for_entity(entity_eid: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output variable
    link_entry = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Retrieve content from the tenant
    try:
        entity_info_response = requests.get(tenant_url + 'api/v1.0/entities/' + entity_eid + '?application=eln',
                                                                headers={'x-api-key': tenant_api_key}
                                                            )
        entity_info_response_content = entity_info_response.json()
        link_entry = entity_info_response_content.get('data').get('link')
    except:
        pass
    # return
    return link_entry