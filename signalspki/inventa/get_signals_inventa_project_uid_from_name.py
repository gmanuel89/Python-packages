#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Get project UID from name
def get_signals_inventa_project_uid_from_name(signals_inventa_project_name:str, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> int:
    # Initialise output
    project_uid = None
    # Retrieve content
    signals_inventa_project_list_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, 'project-service/projects', signals_inventa_tenant_authentication)
    # Get project UID from list
    if signals_inventa_project_list_response_content is not None:
        for prj in signals_inventa_project_list_response_content:
            if str(prj.get('name')).lower() == str(signals_inventa_project_name).lower():
                project_uid = prj.get('uid')
    # return
    return project_uid