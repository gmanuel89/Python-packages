#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import libraries and functions
from signalspki.inventa.get_files_info_in_project import get_files_info_in_project

## Get files info in a Dataset
def get_files_info_in_dataset(project_uid: int, project_revision: int, dataset_uid: int, tenant_url: str, tenant_api_key: str) -> list[dict]:
    # Initialise output
    files_info_in_dataset = []
    # Fix project revision
    if project_revision is None:
        project_revision = 0
    # Retrieve the list of files for the project
    files_in_project = get_files_info_in_project(project_uid, project_revision, tenant_url, tenant_api_key)
    # Get the files for that dataset
    for f in files_in_project:
        if f.get('dataSetUid') == dataset_uid:
            files_info_in_dataset.append(f)
    # return
    return files_info_in_dataset