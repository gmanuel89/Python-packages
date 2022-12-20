#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests

## Get project latest revision number
def get_project_latest_revision_number(project_uid: int, tenant_url: str, tenant_api_key: str) -> int:
    # Initialise output
    project_latest_revision = 0
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_project_revisions_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions',
                                                                    headers={'x-api-key': tenant_api_key})
        signals_inventa_project_revisions_response_content = signals_inventa_project_revisions_response.json()
    except:
        signals_inventa_project_revisions_response_content = None
    # Get latest project revision
    all_project_revisions = []
    if signals_inventa_project_revisions_response_content is not None and isinstance(signals_inventa_project_revisions_response_content, list):
        for prj in signals_inventa_project_revisions_response_content:
            all_project_revisions.append(prj.get('derivedRevisionNumber'))
        project_latest_revision = max(all_project_revisions)
    # return
    return project_latest_revision