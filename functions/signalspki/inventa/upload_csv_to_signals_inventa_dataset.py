#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from functions.signalspki.inventa import *
from functions.signalspki.common import *

## Loads a CSV file into a Signals Inventa dataset
def upload_csv_to_signals_inventa_dataset(input_csv_file: str, input_data_name: str, signals_inventa_project_uid: int, signals_inventa_dataset_uid: int, signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> dict:
    # Initialise output
    file_upload_response = {}
    # Generate the API URL
    tenant_api_url_suffix = '/job-service/projects/' + str(signals_inventa_project_uid) + '/add-file?datasetUid=' + str(signals_inventa_dataset_uid)
    # Generate the payload components for POST request
    payload_for_post_request = {}
    additional_headers = {}
    if not str(input_data_name).endswith('.csv'): input_data_name = input_data_name + '.csv'
    file_to_upload = {'file': (input_data_name, open(input_csv_file, 'rb').read(), 'text/plain')}
    # Upload the CSV file to Signals Inventa
    file_upload_response = post_response_content_from_tenant(signals_inventa_tenant_url, tenant_api_url_suffix, signals_inventa_tenant_authentication, payload_for_post_request, additional_headers, file_to_upload)
    # return
    return file_upload_response