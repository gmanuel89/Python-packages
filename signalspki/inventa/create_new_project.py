#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import funcions and libraries
import requests, json

## Creates a new Inventa project
def create_new_project(project_name: str, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    project_creation_tenant_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Trigger the dataset creation
    try:
        project_creation_tenant_response = requests.post(tenant_url + 'project-service/projects/',
                                                            headers={'x-api-key': tenant_api_key},
                                                            data=json.dumps({'name': project_name, 'projectType': 'v2'})
                                                            )
    except:
        pass
    # return
    return project_creation_tenant_response
