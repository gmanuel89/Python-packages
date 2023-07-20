#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-20
#####

## Import libraries
import requests

## Delete the files from an Inventa Project
def delete_files_from_project(project_uid: int, project_revision: int, file_uid_list: list[int], tenant_url: str, tenant_api_key: str) -> dict[int, requests.Response]:
    # Initialise output
    response_list = {}
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Fix project revision
    if project_revision is None:
        project_revision = 0
    # Delete the file via its UID
    for file_uid in file_uid_list:
        try:
            file_deletion_response = requests.delete(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/files/' + str(file_uid),
                                                    headers={'x-api-key': tenant_api_key})
            response_list[file_uid] = file_deletion_response
        except:
            response_list[file_uid] = None
    # return
    return response_list