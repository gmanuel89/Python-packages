#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-17
#####

### Import functions
import datetime
from signalspki.inventa.create_new_dataset_in_signals_inventa_project import create_new_dataset_in_signals_inventa_project
from signalspki.inventa.get_signals_inventa_project_uid_from_name import get_signals_inventa_project_uid_from_name
from signalspki.inventa.get_signals_inventa_map_id_from_name import get_signals_inventa_map_id_from_name
from signalspki.inventa.associate_map_with_dataset_signals_inventa import associate_map_with_dataset_signals_inventa
from signalspki.inventa.retrieve_datasets_information_for_project import retrieve_datasets_information_for_project

### Get the UID of the dataset where to upload files (existing one or newly created)
def determine_dataset_uid_for_file_upload(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, signals_inventa_project_name: str, signals_inventa_dataset_name: str, signals_inventa_map_name: str, maximum_number_of_files_per_dataset=30) -> int:
    # Initialise output variable
    signals_inventa_dataset_uid = None
    # Retrieve the Project UID
    signals_inventa_project_uid = get_signals_inventa_project_uid_from_name(signals_inventa_project_name, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # Retrieve all the datasets with the desired name, along with the number of files and the UID
    datasets_information = retrieve_datasets_information_for_project(signals_inventa_tenant_url, signals_inventa_tenant_authentication, signals_inventa_project_uid, signals_inventa_dataset_name)
    # Determine the UID of the dataset that can accept the file (based upon its size)
    for dt in datasets_information:
        if dt.get('size') < maximum_number_of_files_per_dataset:
            signals_inventa_dataset_uid = dt.get('uid')
            break
    # If no dataset has been found suitable, create a new one
    if signals_inventa_dataset_uid is None:
        dataset_creation_response = create_new_dataset_in_signals_inventa_project(signals_inventa_dataset_name + ' ' + str(datetime.datetime.now()), signals_inventa_project_uid, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
        signals_inventa_dataset_uid = dataset_creation_response.get('uid')
        # Associate the correct map with the dataset, in any case (maybe it was created empty without map association)
        signals_inventa_map_id = get_signals_inventa_map_id_from_name(signals_inventa_map_name, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
        dataset_map_association_response = associate_map_with_dataset_signals_inventa(signals_inventa_dataset_uid, signals_inventa_map_id, signals_inventa_project_uid, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # return
    return signals_inventa_dataset_uid