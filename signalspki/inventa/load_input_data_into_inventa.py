#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
from signalspki.inventa.get_signals_inventa_project_uid_from_name import get_signals_inventa_project_uid_from_name
from signalspki.inventa.upload_csv_to_signals_inventa_dataset import upload_csv_to_signals_inventa_dataset
from csv_handling.materialise_content_into_csv_file import materialise_content_into_csv_file
from signalspki.inventa.determine_dataset_uid_for_file_upload import determine_dataset_uid_for_file_upload

## Loads the dataset into Signals Inventa
def load_input_data_into_inventa(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict, input_signals_inventa_project_name: str, input_signals_inventa_dataset_name: str, input_signals_inventa_map_name: str, input_data: list[dict], input_data_name: str, maximum_number_of_files_per_dataset: int) -> dict:
    # Get the Project UID from its name
    project_uid = get_signals_inventa_project_uid_from_name(input_signals_inventa_project_name, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    # Determine if a new dataset must be created
    dataset_uid = determine_dataset_uid_for_file_upload(signals_inventa_tenant_url, signals_inventa_tenant_authentication, input_signals_inventa_project_name, input_signals_inventa_dataset_name, input_signals_inventa_map_name, maximum_number_of_files_per_dataset)
    # Add the data to the dataset (materialise the content first into a temporary file)
    input_temporary_csv_file = materialise_content_into_csv_file(input_data)
    csv_upload_response = upload_csv_to_signals_inventa_dataset(input_temporary_csv_file.read(), input_data_name, project_uid, dataset_uid, signals_inventa_tenant_url, signals_inventa_tenant_authentication)
    return csv_upload_response