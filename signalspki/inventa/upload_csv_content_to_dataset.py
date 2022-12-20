#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-05
#####

## Import libraries and functions
import requests

## Loads a CSV file content into a Signals Inventa dataset
def upload_csv_content_to_dataset(input_csv_file_content: str, input_data_name: str, project_uid: int, dataset_uid: int, tenant_url: str, tenant_api_key: str) -> requests.Response:
    # Initialise output
    file_upload_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Name of the relative entry in the Signals Inventa dataset
    if not str(input_data_name).endswith('.csv'):
        input_data_name = input_data_name + '.csv'
    # Encoding to a multipart/form-data body (for API call)
    body, content_type = requests.models.encode_multipart_formdata({'file': (input_data_name, input_csv_file_content, 'text/plain')})
    # Upload the CSV file to Signals Inventa
    try:
        file_upload_response = requests.post(tenant_url + 'job-service/projects/' + str(project_uid) + '/add-file?datasetUid=' + str(dataset_uid),
                                                headers={'x-api-key': tenant_api_key, 'Content-Type': content_type},
                                                data=body)
    except:
        file_upload_response = None
    # return
    return file_upload_response