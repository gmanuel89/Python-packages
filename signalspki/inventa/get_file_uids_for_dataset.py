## Import libraries and functions
from signalspki.inventa.get_files_in_project import get_files_in_project

## Retrieves the file UIDs in a selected Inventa dataset
def get_file_uids_for_dataset(signals_inventa_project_uid: int, signals_inventa_dataset_uid: int, signals_inventa_tenant_url: str, signals_inventa_api_key: str):
    # Initialise output
    files_in_dataset = []
    # Retrieve the list of files for the project
    files_in_project = get_files_in_project(signals_inventa_project_uid, 0, signals_inventa_tenant_url, signals_inventa_api_key)
    # Get the files for that dataset
    for f in files_in_project:
        if f.get('dataSetUid') == signals_inventa_dataset_uid:
            files_in_dataset.append(f)
    # return
    return files_in_dataset
