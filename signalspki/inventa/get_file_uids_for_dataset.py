## Import libraries and functions
from signalspki.inventa.get_files_info_in_project import get_files_info_in_project

## Retrieves the file UIDs in a selected Inventa dataset
def get_file_uids_for_dataset(project_uid: int, dataset_uid: int, tenant_url: str, tenant_api_key: str) -> list[dict]:
    # Initialise output
    files_in_dataset = []
    # Fix project revision
    if project_revision is None:
        project_revision = 0
    # Retrieve the list of files for the project
    files_in_project = get_files_info_in_project(project_uid, 0, tenant_url, tenant_api_key)
    # Get the files for that dataset
    for f in files_in_project:
        if f.get('dataSetUid') == dataset_uid:
            files_in_dataset.append(f)
    # return
    return files_in_dataset
