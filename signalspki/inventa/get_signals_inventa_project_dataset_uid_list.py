#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.inventa.get_signals_inventa_project_uid_from_name import get_signals_inventa_project_uid_from_name
from signalspki.inventa.get_signals_inventa_project_latest_revision import get_signals_inventa_project_latest_revision
from signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Retrieves the list of dataset IDs for a Project revision
def get_signals_inventa_project_dataset_uid_list(signals_inventa_project_name: str, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, signals_inventa_project_revision=None) -> list[str]:
    # Initialise output
    dataset_uid_list = []
    # Get project UID
    project_uid = get_signals_inventa_project_uid_from_name(signals_inventa_project_name, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # Get latest revision if not specified
    if signals_inventa_project_revision is None or signals_inventa_project_revision == 0:
        signals_inventa_project_revision = get_signals_inventa_project_latest_revision(signals_inventa_project_name, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # Retrieve content
    tenant_api_url_suffix = '/project-service/projects/' + str(project_uid) + '/revisions/' + str(signals_inventa_project_revision) + '/datasets'
    signals_inventa_project_datasets_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication)
    for ds in signals_inventa_project_datasets_response_content.get('datasets'):
        dataset_uid_list.append(ds.get('uid'))
    # return
    return dataset_uid_list