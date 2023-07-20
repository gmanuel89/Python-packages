#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-07-18
#####

## Import libraries
import requests

## Retrieves the list of attachments for a Project revision with all their information
def get_attachments_info_list_for_project(project_uid: int, tenant_url: str, tenant_api_key: str, project_revision=0) -> list[dict]:
    # Initialise output
    attachment_info_list = []
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Use revision "0" if not specified (revision "0" gets all the datasets, even if not loaded)
    if project_revision is None:
        project_revision = 0
    # Retrieve content
    try:
        attachments_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/attachments',
                                                                    headers={'x-api-key': tenant_api_key})
        attachment_info_list = attachments_response.json()
    except:
        pass
    # return
    return attachment_info_list