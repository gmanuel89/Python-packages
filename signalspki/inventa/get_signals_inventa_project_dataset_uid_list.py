#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-06
#####

## Import libraries and functions
import requests
from signalspki.inventa.get_signals_inventa_project_uid_from_name import get_signals_inventa_project_uid_from_name
from signalspki.inventa.get_signals_inventa_project_latest_revision import get_signals_inventa_project_latest_revision

## Retrieves the list of dataset IDs for a Project revision
def get_signals_inventa_project_dataset_uid_list(signals_inventa_project_name: str, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, signals_inventa_project_revision=None) -> list[str]:
    # Initialise output
    dataset_uid_list = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Get project UID
    project_uid = get_signals_inventa_project_uid_from_name(signals_inventa_project_name, signals_inventa_tenant_url, signals_inventa_tenant_api_key)
    # Get latest revision if not specified
    if signals_inventa_project_revision is None or signals_inventa_project_revision == 0:
        signals_inventa_project_revision = get_signals_inventa_project_latest_revision(signals_inventa_project_name, signals_inventa_tenant_url, signals_inventa_tenant_api_key)
    # Retrieve content
    tenant_api_url_suffix = '/project-service/projects/' + str(project_uid) + '/revisions/' + str(signals_inventa_project_revision) + '/datasets'
    try:
        signals_inventa_project_datasets_response = requests.get(signals_inventa_tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/' + str(signals_inventa_project_revision) + '/datasets',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_project_datasets_response_content = signals_inventa_project_datasets_response.json()
        # Retrieve the Project UID list
        for ds in signals_inventa_project_datasets_response_content.get('datasets'):
            dataset_uid_list.append(ds.get('uid'))
    except:
        signals_inventa_project_datasets_response_content = None
    # return
    return dataset_uid_list