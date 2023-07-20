#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-01-11
#####

### Import functions
import datetime
from signals.inventa.create_new_dataset_in_project import create_new_dataset_in_project
from signals.inventa.get_project_uid_from_name import get_project_uid_from_name
from signals.inventa.get_map_id_from_name import get_map_id_from_name
from signals.inventa.associate_map_with_dataset import associate_map_with_dataset
from signals.inventa.retrieve_datasets_information_for_project import retrieve_datasets_information_for_project

### Get the UID of the dataset where to upload files (existing one or newly created)
def determine_dataset_uid_for_file_upload(tenant_url: str, tenant_api_key: str, project_uid: int, dataset_name: str, map_id: str, maximum_number_of_files_per_dataset=30) -> int:
    # Initialise output variable
    dataset_uid = None
    # Retrieve all the datasets with the desired name, along with the number of files and the UID
    datasets_information = retrieve_datasets_information_for_project(tenant_url, tenant_api_key, project_uid, dataset_name)
    # Determine the UID of the dataset that can accept the file (based upon its size)
    for dt in datasets_information:
        if dt.get('size') < maximum_number_of_files_per_dataset:
            dataset_uid = dt.get('uid')
            break
    # If no dataset has been found suitable, create a new one
    if dataset_uid is None:
        dataset_creation_response = create_new_dataset_in_project(dataset_name + ' ' + str(datetime.datetime.now()), project_uid, tenant_url, tenant_api_key)
        if dataset_creation_response is not None:
            dataset_uid = dataset_creation_response.json().get('uid')
            # Associate the correct map with the dataset, in any case (maybe it was created empty without map association)
            if map_id is not None:
                dataset_map_association_response = associate_map_with_dataset(dataset_uid, map_id, project_uid, tenant_url, tenant_api_key)
    # return
    return dataset_uid