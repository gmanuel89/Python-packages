#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-22
#####

## Import libraries
import requests, json

## Load all the Datasets in a Project
def load_project(tenant_url: str, tenant_api_key: str, project_uid: int, force_load_all=False) -> requests.Response:
    # Initialise output
    project_load_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Trigger the project load
    # Force load all
    if force_load_all:
        try:
            project_load_response = requests.post(tenant_url + 'job-service/load',
                                                    headers={'x-api-key': tenant_api_key},
                                                    data=json.dumps({'definition': {'projectUID': project_uid, 'debug': True, 'mode': 'loadAll'}})
                                                )
        except:
            project_load_response = None
    else:
        # Try with loadNew and fall back on loadAll if not possible
        try:
            project_load_response = requests.post(tenant_url + 'job-service/load',
                                                    headers={'x-api-key': tenant_api_key},
                                                    data=json.dumps({'definition': {'projectUID': project_uid, 'debug': True, 'mode': 'loadNew'}})
                                                )
        except:
            project_load_response = None
        if (isinstance(project_load_response, str) and '"statusCode":405' in project_load_response) or (isinstance(project_load_response, dict) and project_load_response.get('statusCode') == 405):
            try:
                project_load_response = requests.post(tenant_url + 'job-service/load',
                                                    headers={'x-api-key': tenant_api_key},
                                                    data=json.dumps({'definition': {'projectUID': project_uid, 'debug': True, 'mode': 'loadAll'}})
                                                )
            except:
                project_load_response = None
    # return
    return project_load_response