#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.inventa.get_signals_inventa_project_uid_from_name import get_signals_inventa_project_uid_from_name
from functions.signalspki.inventa.get_signals_inventa_map_id_from_name import get_signals_inventa_map_id_from_name
from functions.signalspki.inventa.get_signals_inventa_project_latest_revision import get_signals_inventa_project_latest_revision
from functions.signalspki.inventa.get_signals_inventa_project_dataset_list import get_signals_inventa_project_dataset_list
from functions.signalspki.inventa.get_signals_inventa_project_dataset_uid_from_name import get_signals_inventa_project_dataset_uid_from_name
from functions.signalspki.inventa.create_new_dataset_in_signals_inventa_project import create_new_dataset_in_signals_inventa_project
from functions.signalspki.inventa.associate_map_with_dataset_signals_inventa import associate_map_with_dataset_signals_inventa
from functions.signalspki.inventa.upload_csv_to_signals_inventa_dataset import upload_csv_to_signals_inventa_dataset
from functions.csv_handling.materialise_content_into_csv_file import materialise_content_into_csv_file

## Loads the dataset into Signals Inventa
def load_input_data_into_inventa(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, input_signals_inventa_project_name: str, input_signals_inventa_dataset_name: str, input_signals_inventa_map_name: str, input_data: list[dict], input_data_name: str) -> dict:
    # Get the Project UID from its name
    project_uid = get_signals_inventa_project_uid_from_name(input_signals_inventa_project_name, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # Get Map ID
    map_id = get_signals_inventa_map_id_from_name(input_signals_inventa_map_name, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # Retrieve project latest revision
    project_latest_revision = get_signals_inventa_project_latest_revision(project_uid, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # Determine if a new dataset must be created
    project_dataset_list = get_signals_inventa_project_dataset_list(project_uid, signals_inventa_tenant_url, signals_inventa_tenant_authentication, 0)
    if str(input_signals_inventa_dataset_name) in project_dataset_list:
        # Get Dataset ID
        dataset_uid = get_signals_inventa_project_dataset_uid_from_name(input_signals_inventa_dataset_name, input_signals_inventa_project_name, project_latest_revision, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
        pass
    else:
        # Create a new dataset (and retrieve its UID)
        dataset_creation_response = create_new_dataset_in_signals_inventa_project(input_signals_inventa_dataset_name, project_uid, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
        dataset_uid = dataset_creation_response.get('uid')
        # Associate a map to the dataset
        dataset_map_association = associate_map_with_dataset_signals_inventa(dataset_uid, map_id, project_uid, project_latest_revision, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # Add the data to the dataset (materialise the content first into a temporary file)
    input_temporary_csv_file = materialise_content_into_csv_file(input_data)
    csv_upload_response = upload_csv_to_signals_inventa_dataset(input_temporary_csv_file, input_data_name, project_uid, dataset_uid, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    return csv_upload_response