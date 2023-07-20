#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-11-13
#####

## Import libraries and functions
import requests, json

## Create a ADT template in Signals Notebook config (core session cookie or bearer token needed)
def create_new_grid_template(grid_name: str, tenant_url: str, tenant_core_session_cookie_id: str, tenant_bearer_token: str) -> str:
    # Initialise output
    new_table_eid = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
      tenant_url = tenant_url + '/'
    # Formulate the payload JSON
    payload_for_post_request = {}
    payload_for_post_request['data'] = {}
    payload_for_post_request['type'] = 'grid'
    payload_for_post_request['name'] = str(grid_name)
    payload_for_post_request['description'] = ''
    payload_for_post_request['flags'] = {}
    payload_for_post_request['flags']['isTemplate'] = True
    payload_for_post_request['flags']['isSystem'] = True
    payload_for_post_request['ancestors'] = []
    # Headers for API call
    headers_for_api_call = {}
    if tenant_bearer_token:
        headers_for_api_call = {'Authorization': 'Bearer ' + str(tenant_bearer_token)}
    elif tenant_core_session_cookie_id:
        if not tenant_core_session_cookie_id.startswith('CORE_SESSION='):
            tenant_core_session_cookie_id = 'CORE_SESSION=' + tenant_core_session_cookie_id
        headers_for_api_call = {'Cookie': tenant_core_session_cookie_id}
    # Post csv content to SNB table
    try:
        tenant_post_response = requests.post(tenant_url + 'api/v1.0/entities?application=eln',
                                            headers=headers_for_api_call,
                                            data=json.dumps(payload_for_post_request))
        tenant_post_response_content = tenant_post_response.json()
        new_table_eid = tenant_post_response_content.get('eid')
    except:
        print('Cannot POST content to tenant %s' %(tenant_url))
        print('Payload: ' + json.dumps(payload_for_post_request))
        pass
    # return
    return new_table_eid


"""
PAYLOAD
{
    "type": "grid",
    "data": null,
    "name": "Test ADT",
    "description": "",
    "flags": {
        "isTemplate": true,
        "isSystem": true
    },
    "ancestors": []
}
"""
