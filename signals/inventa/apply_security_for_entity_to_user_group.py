#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-28
#####

## Import libraries
import requests, json

## Applies the security to a specific user group for a specific entity
def apply_security_for_entity_to_user_group(user_group_uuid: str, target_entity: str, security_query_json: str, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    tenant_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Return immediately if no entity or groups or security JSON have been specified
    if (target_entity is None or target_entity == '') or (user_group_uuid is None or user_group_uuid == '') or (security_query_json is None or security_query_json == ''):
        return tenant_response
    # Formulate payload for POST request
    payload_for_post_request = {}
    # Entity
    payload_for_post_request['entity'] = target_entity.capitalize()
    # Group
    payload_for_post_request['groupID'] = user_group_uuid
    # Search Query (convert the string JSON to a dictionary first)
    payload_for_post_request['search'] = {}
    payload_for_post_request['search']['@innerHits'] = {}
    payload_for_post_request['search']['@entity'] = target_entity.capitalize()
    try:
        payload_for_post_request['search']['@query'] = json.loads(security_query_json.strip().replace('\n', '').replace('\t', ''))
    except:
        payload_for_post_request['search']['@query'] = {}
    # Apply security to tenant
    try:
        tenant_response = requests.post(tenant_url + 'search-service/search-security-permissions',
                                        headers={'x-api-key': tenant_api_key},
                                        json=payload_for_post_request)
    except:
        pass
    # return
    return tenant_response
