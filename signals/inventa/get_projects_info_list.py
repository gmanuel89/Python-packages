#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-05-26
#####

## Import libraries
import requests

## Get list of project JSONs from Signals Inventa tenant
def get_projects_info_list(tenant_url: str, tenant_api_key: str) -> list[dict]:
    # Initialise output
    projects_info_list = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content
    try:
        project_list_response = requests.get(tenant_url + 'project-service/projects/details',
                                                                    headers={'x-api-key': tenant_api_key})
        projects_info_list = project_list_response.json()
    except:
        pass
    # return
    return projects_info_list