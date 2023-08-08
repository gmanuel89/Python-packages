#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-08-08
#####

## Import libraries
import requests

## Get project revision numbers
def get_project_revision_numbers(project_uid: int, tenant_url: str, tenant_api_key: str) -> int:
    # Initialise output
    project_revision_numbers = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content
    try:
        project_revisions_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions',
                                                                    headers={'x-api-key': tenant_api_key})
        project_revisions_response_content = project_revisions_response.json()
        # Get project revisions
        for prj in project_revisions_response_content:
            project_revision_numbers.append(prj.get('derivedRevisionNumber'))
    except:
        pass
    # return
    return project_revision_numbers