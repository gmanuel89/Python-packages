#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-17
#####

## Import libraries and functions
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Get project UID from name
def get_signals_inventa_project_latest_revision(signals_inventa_project_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> int:
    # Initialise output
    project_latest_revision = 0
    # Retrieve content
    tenant_api_url_suffix = '/project-service/projects/' + str(signals_inventa_project_uid) + '/revisions' 
    signals_inventa_project_revisions_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication)
    # Get latest project revision
    all_project_revisions = []
    if signals_inventa_project_revisions_response_content is not None and isinstance(signals_inventa_project_revisions_response_content, list):
        for prj in signals_inventa_project_revisions_response_content:
            all_project_revisions.append(prj.get('derivedRevisionNumber'))
        project_latest_revision = max(all_project_revisions)
    # return
    return project_latest_revision