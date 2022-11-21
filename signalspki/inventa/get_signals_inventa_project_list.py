#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Get list of projects from Signals Inventa tenant
def get_signals_inventa_project_list(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> list:
    # Initialise output
    project_list = []
    # Retrieve content
    signals_inventa_project_list_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, '/project-service/projects', signals_inventa_tenant_authentication)
    # Get project list
    if signals_inventa_project_list_response_content is not None:
        for prj in signals_inventa_project_list_response_content:
            project_list.append(prj.get('name'))
    # return
    return project_list