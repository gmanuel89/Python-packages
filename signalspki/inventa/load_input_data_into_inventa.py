#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-01-11
#####

## Import libraries and functions
import requests
from signalspki.inventa.get_project_uid_from_name import get_project_uid_from_name
from signalspki.inventa.upload_csv_content_to_dataset import upload_csv_content_to_dataset
from csv_handling.materialise_content_into_csv_file import materialise_content_into_csv_file
from signalspki.inventa.determine_dataset_uid_for_file_upload import determine_dataset_uid_for_file_upload

## Loads the dataset into Signals Inventa
def load_input_data_into_inventa(tenant_url: str, tenant_api_key: str, project_uid: int, dataset_name: str, map_id: str, input_data: list[dict], input_data_name: str, maximum_number_of_files_per_dataset: int) -> requests.Response:
    # Determine if a new dataset must be created
    dataset_uid = determine_dataset_uid_for_file_upload(tenant_url, tenant_api_key, project_uid, dataset_name, map_id, maximum_number_of_files_per_dataset)
    # Add the data to the dataset (materialise the content first into a temporary file)
    input_temporary_csv_file = materialise_content_into_csv_file(input_data)
    csv_upload_response = upload_csv_content_to_dataset(input_temporary_csv_file.read(), input_data_name, project_uid, dataset_uid, tenant_url, tenant_api_key)
    return csv_upload_response