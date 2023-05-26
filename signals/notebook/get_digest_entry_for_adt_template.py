#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-14
#####

## Import libraries and functions
import requests

## Get the Digest entry from the ADT template retrieval response 
def get_digest_entry_for_adt_template(adt_eid: str, tenant_url: str, tenant_core_session_cookie_id: str) -> str:
    # Initialise output variable
    digest_entry = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Retrieve content from the tenant
    try:
        entity_info_response = requests.get(tenant_url + 'api/v1.0/entities/' + adt_eid + '?application=eln',
                                            headers={'Cookie': tenant_core_session_cookie_id}
                                            )
        entity_info_response_content = entity_info_response.json()
        digest_entry = str(entity_info_response_content.get('digest'))
    except:
        pass
    # return
    return digest_entry