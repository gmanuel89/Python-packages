#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-11-30
#####

## Import libraries and functions
import requests
import json

## Create a table in Signals Notebook (under a specified ancestor entity)
def create_new_grid(grid_name: str, ancestor_eid: str, template_eid: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output
    new_table_eid = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
      pass
    else:
      tenant_url = tenant_url + '/'
    # Formulate the payload JSON
    payload_for_post_request = {}
    payload_for_post_request['data'] = {}
    payload_for_post_request['data']['type'] = 'grid'
    payload_for_post_request['data']['attributes'] = {'name' : str(grid_name)}
    payload_for_post_request['data']['relationships'] = {}
    payload_for_post_request['data']['relationships']['ancestors'] = {}
    payload_for_post_request['data']['relationships']['ancestors']['data'] = []
    payload_for_post_request['data']['relationships']['ancestors']['data'].append({'type' : 'experiment', 'id' : ancestor_eid})
    payload_for_post_request['data']['relationships']['template'] = {}
    payload_for_post_request['data']['relationships']['template']['data'] = {'type' : 'grid', 'id' : template_eid}
    # Post csv content to SNB table
    try:
        tenant_post_response = requests.post(tenant_url + 'api/rest/v1.0/entities?force=true',
                                            headers={'x-api-key':tenant_api_key},
                                            data=json.dumps(payload_for_post_request))
        tenant_post_response_content = tenant_post_response.json()
        new_table_eid = tenant_post_response_content.get('data').get('id')
    except:
        print('Cannot POST content to tenant %s' %(tenant_url))
        print('Payload: ' + json.dumps(payload_for_post_request))
        pass
    # return
    return new_table_eid


"""
{
  "data": {
    "type": "grid",
    "attributes": {
      "name": "AXX - AnChem - HPLC peaks{*}"
    },
    "relationships": {
      "ancestors": {
        "data": [
          {
            "type": "experiment",
            "id": "experiment:eaf98811-3e4f-419e-905e-9da365067181"
          }
        ]
      },
      "template": {
        "data": {
          "type": "grid",
          "id": "grid:ae3c9e1e-8567-4b35-9c6d-9febfafe3c90"
        }
      }
    }
  }
}
"""
