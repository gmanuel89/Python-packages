#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-07-17
#####

## Import libraries
import requests

## Get the file in a Project via its UID
def get_file_content_from_uid(project_uid: int, project_revision: int, file_uid: int, tenant_url: str, tenant_api_key: str) -> bytes | None:
    # Initialise output
    file_content = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Fix project revision
    if project_revision is None:
        project_revision = 0
    # Retrieve content
    try:
        project_file_response = requests.get(tenant_url + 'export-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/files/' + str(file_uid) + '/download',
                                            headers={'x-api-key': tenant_api_key})
        file_content = project_file_response.content
    except:
        file_content = None
    # return
    return file_content