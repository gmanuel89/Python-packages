#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

### Import functions
import datetime
from signalspki.inventa.create_new_dataset_in_project import create_new_dataset_in_project
from signalspki.inventa.get_project_uid_from_name import get_project_uid_from_name
from signalspki.inventa.get_map_id_from_name import get_map_id_from_name
from signalspki.inventa.associate_map_with_dataset import associate_map_with_dataset
from signalspki.inventa.retrieve_datasets_information_for_project import retrieve_datasets_information_for_project

### Get the UID of the dataset where to upload files (existing one or newly created)
def determine_dataset_uid_for_file_upload(tenant_url: str, tenant_api_key: str, project_name: str, dataset_name: str, map_name: str, maximum_number_of_files_per_dataset=30) -> int:
    # Initialise output variable
    dataset_uid = None
    # Retrieve the Project UID
    project_uid = get_project_uid_from_name(project_name, tenant_url, tenant_api_key)
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
            signals_inventa_map_id = get_map_id_from_name(map_name, tenant_url, tenant_api_key)
            if signals_inventa_map_id is not None:
                dataset_map_association_response = associate_map_with_dataset(dataset_uid, signals_inventa_map_id, project_uid, tenant_url, tenant_api_key)
    # return
    return dataset_uid