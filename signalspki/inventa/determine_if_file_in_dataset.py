## Import libraries
import hashlib
from signalspki.inventa.get_files_info_in_dataset import get_files_info_in_dataset

## Determine if a provided file is already contained in the dataset
def determine_if_file_in_dataset(tenant_url: str, tenant_api_key: str, project_uid: int, project_revision: int, dataset_uid: int, file_name: str, file_content: str) -> bool:
    # Initialise output
    file_in_dataset = False
    # Fix project revision
    if project_revision is None:
        project_revision = 0
    # Retrieve all the files in the project
    files_info_in_dataset = get_files_info_in_dataset(project_uid, project_revision, dataset_uid, tenant_url, tenant_api_key)
    # Find a match (filename)
    if file_name is not None and file_content is None:
        for dtfile in files_info_in_dataset:
            if dtfile.get('filename') == file_name:
                file_in_dataset = True
                break
    # Find a match (filename and content checksum)
    elif file_name is not None and file_content is not None:
        for dtfile in files_info_in_dataset:
            if dtfile.get('filename') == file_name:
                hash_existing_file = hashlib.md5(str(dtfile.get('fileContent')).encode()).hexdigest()
                hash_input_file = hashlib.md5(str(file_content).encode()).hexdigest()
                if hash_existing_file == hash_input_file:
                    file_in_dataset = True
                    break
    # Find a match (content checksum)
    elif file_name is None and file_content is not None:
        for dtfile in files_info_in_dataset:
            hash_existing_file = hashlib.md5(dtfile.get('fileContent')).hexdigest()
            hash_input_file = hashlib.md5(file_content).hexdigest()
            if hash_existing_file == hash_input_file:
                file_in_dataset = True
                break
    # no match
    else:
        file_in_dataset = False
    # return
    return file_in_dataset