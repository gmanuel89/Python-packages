#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-10
#####

## Import libraries and functions
import io
from functions.signalspki.common.post_response_content_from_tenant import post_response_content_from_tenant

## Loads a CSV file into a Signals Inventa dataset
def upload_csv_to_signals_inventa_dataset(input_csv_file: str | io.TextIOWrapper, input_data_name: str, signals_inventa_project_uid: int, signals_inventa_dataset_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> dict:
    # Initialise output
    file_upload_response = {}
    # Generate the API URL
    tenant_api_url_suffix = '/job-service/projects/' + str(signals_inventa_project_uid) + '/add-file?datasetUid=' + str(signals_inventa_dataset_uid)
    # Generate the payload components for POST request
    payload_for_post_request = {}
    additional_headers = {}
    if not str(input_data_name).endswith('.csv'): input_data_name = input_data_name + '.csv'
    # File handling (path or file wrapper)
    if isinstance(input_csv_file, str):
        file_to_upload = {'file': (input_data_name, open(input_csv_file, 'rb').read(), 'text/plain')}
    elif isinstance(input_csv_file, io.TextIOWrapper):
        # Rewind the temporary file
        input_csv_file.seek(0)
        file_to_upload = {'file': (input_data_name, input_csv_file.read(), 'text/plain')}
    else:
        file_to_upload = {}
    # Upload the CSV file to Signals Inventa
    file_upload_response = post_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, payload_for_post_request, additional_headers, file_to_upload)
    # return
    return file_upload_response