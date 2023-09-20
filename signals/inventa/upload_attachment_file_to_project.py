#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-09-20
#####

## Import libraries
import requests

## Upload a file to an Inventa project as attachment
def upload_attachment_file_to_project(attachment_file_path: str, project_uid: int, tenant_url: str, tenant_api_key: str, attachment_file_name: str, attachment_file_label=None) -> requests.Response:
    # Initialise output
    file_upload_response = None
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    try:
        # Encoding to a multipart/form-data body (for API call)
        body, content_type = requests.models.encode_multipart_formdata({'file': (attachment_file_name, open(attachment_file_path, 'rb').read())})
        # Upload the CSV file to Signals Inventa
        file_upload_response = requests.post(tenant_url + 'project-service/projects/' + str(project_uid) + '/attachment',
                                                headers={'x-api-key': tenant_api_key, 'Content-Type': content_type},
                                                data=body)
    except:
        pass
    # return
    return file_upload_response
