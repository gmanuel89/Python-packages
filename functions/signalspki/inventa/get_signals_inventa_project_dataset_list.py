#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.inventa.get_signals_inventa_project_latest_revision import get_signals_inventa_project_latest_revision
from functions.signalspki.common.get_response_content_from_tenant import get_response_content_from_tenant

## Retrieves the list of dataset for a Project revision
def get_signals_inventa_project_dataset_list(signals_inventa_project_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, signals_inventa_project_revision=None) -> list[str]:
    # Initialise output
    dataset_list = []
    # Get latest revision if not specified
    if signals_inventa_project_revision is None or signals_inventa_project_revision == 0:
        signals_inventa_project_revision = get_signals_inventa_project_latest_revision(signals_inventa_project_uid, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # Retrieve content
    tenant_api_url_suffix = '/project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/' + str(signals_inventa_project_revision) + '/datasets'
    signals_inventa_project_datasets_response_content = get_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication)
    for ds in signals_inventa_project_datasets_response_content.get('datasets'):
        dataset_list.append(ds.get('name'))
    # return
    return dataset_list