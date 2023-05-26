#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-21
#####

## Import libraries
import requests

## Get project UID from name
def get_project_uid_from_name(project_name:str, tenant_url: str, tenant_api_key: str) -> int:
    # Initialise output
    project_uid = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content
    try:
        project_list_response = requests.get(tenant_url + 'project-service/projects',
                                            headers={'x-api-key': tenant_api_key})
        project_list_response_content = project_list_response.json()
        # Get project UID from list
        for prj in project_list_response_content:
            if str(prj.get('name')).lower() == str(project_name).lower():
                project_uid = prj.get('uid')
    except:
        pass
    # return
    return project_uid