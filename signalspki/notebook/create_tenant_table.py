#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-29
#####

## Import libraries and functions
import requests
import json
from signalspki.notebook.get_template_grid_name_from_eid import *

## Create a table in Signals Notebook (under a specified ancestor entity)
def create_tenant_table(ancestor_eid: str, template_eid: str, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    tenant_post_response = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
      pass
    else:
      tenant_url = tenant_url + '/'
    # Perform the POST request (row by row)
    # Get the template grid name from EID
    template_grid_name = get_template_grid_name_from_eid(template_eid, tenant_url, tenant_api_key)
    # Formulate the payload JSON
    payload_for_post_request = {}
    payload_for_post_request['data'] = {}
    payload_for_post_request['data']['type'] = 'grid'
    payload_for_post_request['data']['attributes'] = {'name' : str(template_grid_name) + '{*}'}
    payload_for_post_request['data']['relationships'] = {}
    payload_for_post_request['data']['relationships']['ancestors'] = {}
    payload_for_post_request['data']['relationships']['ancestors']['data'] = []
    payload_for_post_request['data']['relationships']['ancestors']['data'].append({'type' : 'experiment', 'id' : ancestor_eid})
    payload_for_post_request['data']['relationships']['template'] = {}
    payload_for_post_request['data']['relationships']['template']['data'] = {'type' : 'grid', 'id' : template_eid}
    # Post csv content to SNB table
    payload_for_post_request_json = json.dumps(payload_for_post_request)
    try:
        tenant_post_response = requests.post(tenant_url_api = tenant_url + '/api/rest/v1.0/entities?force=true',
                                            headers={'x-api-key':tenant_api_key},
                                            data=payload_for_post_request_json)
    except:
        print('Cannot POST content to tenant %s' %(tenant_url))
        print('Payload: ' + payload_for_post_request_json)
        pass
    # return
    return tenant_post_response


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
