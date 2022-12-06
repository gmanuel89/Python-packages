#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-30
#####

# Import libraries and functions
import requests
import json

# TODO set automatic mandatory parameters for experiment creation
# Create an Experiment in Signals Notebook (under a specified ancestor entity)
def create_new_experiment(experiment_name: str, notebook_eid: str, template_eid: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output
    new_experiment_eid = None
    # Fix tenant URL
    if tenant_url.endswith('/'):
        pass
    else:
        tenant_url = tenant_url + '/'
    # Formulate the payload JSON
    payload_for_post_request = {}
    payload_for_post_request['data'] = {}
    payload_for_post_request['data']['type'] = 'experiment'
    payload_for_post_request['data']['attributes'] = {
        'name': str(experiment_name)}
    if notebook_eid is not None and notebook_eid != '':
        payload_for_post_request['data']['relationships'] = {}
        payload_for_post_request['data']['relationships']['ancestors'] = {}
        payload_for_post_request['data']['relationships']['ancestors']['data'] = []
        payload_for_post_request['data']['relationships']['ancestors']['data'].append(
            {'type': 'journal', 'id': notebook_eid})
    if template_eid is not None and template_eid != '':
        payload_for_post_request['data']['relationships']['template'] = {}
        payload_for_post_request['data']['relationships']['template']['data'] = {
            'type': 'experiment', 'id': template_eid}
    # Call the tenant API to create experiment
    try:
        tenant_post_response = requests.post(tenant_url + 'api/rest/v1.0/entities?force=true',
                                             headers={
                                                 'x-api-key': tenant_api_key},
                                             data=json.dumps(payload_for_post_request))
        # If the notebook name is auto-generated by settigs, this creation will fail, therefore we use the Description as the notebook name
        if tenant_post_response.ok:
            tenant_post_response_content = tenant_post_response.json()
        else:
            payload_for_post_request['data']['attributes'] = {
                'description': str(experiment_name)}
            tenant_post_response = requests.post(tenant_url + 'api/rest/v1.0/entities?force=true',
                                                 headers={
                                                     'x-api-key': tenant_api_key},
                                                 data=json.dumps(
                                                     payload_for_post_request)
                                                 )
            tenant_post_response_content = tenant_post_response.json()
        # Retrieve the ID of the new notebook created
        new_experiment_eid = tenant_post_response_content.get('data').get('id')
    except:
        print('Cannot POST content to tenant %s' % (tenant_url))
        print('Payload: ' + json.dumps(payload_for_post_request))
        pass
    # return
    return new_experiment_eid


"""
{
  "data": {
    "type": "experiment",
    "attributes": {
      "name": "Experiment test"
    },
    "relationships": {
      "ancestors": {
        "data": [
          {
            "type": "journal",
            "id": "journal:eaf98811-3e4f-419e-905e-9da365067181"
          }
        ]
      },
      "template": {
        "data": {
          "type": "experiment",
          "id": "experiment:ae3c9e1e-8567-4b35-9c6d-9febfafe3c90"
        }
      }
    }
  }
}
"""