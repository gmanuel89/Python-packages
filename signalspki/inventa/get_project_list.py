#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries
import requests

## Get list of projects from Signals Inventa tenant
def get_project_list(tenant_url: str, tenant_api_key: str) -> list[str]:
    # Initialise output
    project_list = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content
    try:
        project_list_response = requests.get(tenant_url + 'project-service/projects',
                                                                    headers={'x-api-key': tenant_api_key})
        project_list_response_content = project_list_response.json()
    except:
        project_list_response_content = None
    # Get project list
    if project_list_response_content is not None:
        for prj in project_list_response_content:
            project_list.append(prj.get('name'))
    # return
    return project_list