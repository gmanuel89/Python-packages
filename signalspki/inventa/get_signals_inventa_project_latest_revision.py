#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests

## Get project UID from name
def get_signals_inventa_project_latest_revision(signals_inventa_project_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> int:
    # Initialise output
    project_latest_revision = 0
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_project_revisions_response = requests.get(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
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