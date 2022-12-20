#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests

## Retrieve the Project status
def get_project_status(tenant_url: str, tenant_api_key: str, project_uid: int) -> str:
    # Initialise output
    project_load_status = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content
    try:
        project_status_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '?getLoadOptions=true',
                                                headers={'x-api-key': tenant_api_key})
        project_status_response_content = project_status_response.json()
        # Retrieve the status of the project ("loadStatus")
        project_load_status = project_status_response_content.get('loadStatus')
    except:
        project_status_response = None
    # return
    return project_load_status