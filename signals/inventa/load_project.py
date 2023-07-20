#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
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
        # Try with loadNew...
        try:
            project_load_response = requests.post(tenant_url + 'job-service/load',
                                                    headers={'x-api-key': tenant_api_key},
                                                    data=json.dumps({'definition': {'projectUID': project_uid, 'debug': True, 'mode': 'loadNew'}})
                                                )
        except:
            project_load_response = None
        # ...and fall back on loadAll if not possible
        if project_load_response is not None and project_load_response.status_code == 405:
            try:
                project_load_response = requests.post(tenant_url + 'job-service/load',
                                                    headers={'x-api-key': tenant_api_key},
                                                    data=json.dumps({'definition': {'projectUID': project_uid, 'debug': True, 'mode': 'loadAll'}})
                                                )
            except:
                project_load_response = None
    # return
    return project_load_response