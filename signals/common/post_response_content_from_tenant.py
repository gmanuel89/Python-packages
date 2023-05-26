#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-11-10
#####

## Import libraries and functions
from signals.common.formulate_headers_for_tenant_call import formulate_headers_for_tenant_call
import requests

## POST to a tenant and get the response from the tenant
def post_response_content_from_tenant(tenant_url: str, tenant_api_url_suffix: str, tenant_authentication: dict, payload_for_post_request: dict | str, additional_headers={}, file_to_upload={}, output_type='json') -> dict | str | requests.Response:
    # Initialise output variable
    tenant_response_content = None
    # Formulate headers
    headers_api_call = formulate_headers_for_tenant_call(authentication_type=tenant_authentication.get('authentication_type'), authentication_parameters=tenant_authentication.get('authentication_parameters'))
    if additional_headers:
        headers_api_call = headers_api_call | additional_headers
    # Formulate the API URL (remove the '/' from the tenant URL end and from the suffix beginning)
    if tenant_url.endswith('/'):
        tenant_url = tenant_url[0:len(tenant_url)-1]
    if tenant_api_url_suffix.startswith('/'):
        tenant_api_url_suffix = tenant_api_url_suffix[1:len(tenant_api_url_suffix)]
    tenant_api_url = tenant_url + '/' + tenant_api_url_suffix
    # Call the API
    try:
        # with files to upload
        if len(file_to_upload) > 0:
            # encode the payload body for file upload
            body, content_type = requests.models.encode_multipart_formdata(file_to_upload)
            # fix the headers
            headers_api_call = headers_api_call | {'Content-Type': content_type}
            # make the POST call
            tenant_response = requests.post(tenant_api_url, headers=headers_api_call, data=body)
        # with payload
        elif len(payload_for_post_request) > 0:
            tenant_response = requests.post(tenant_api_url, headers=headers_api_call, data=payload_for_post_request)
        # without files to upload or payload
        else:
            tenant_response = requests.post(tenant_api_url, headers=headers_api_call, json={})
        # Collect response
        if tenant_response.ok:
            # json format
            if str(output_type).lower() == 'json':
                tenant_response_content = tenant_response.json()
            # Response object
            elif str(output_type).lower() == 'response':
                tenant_response_content = tenant_response
            # raw text file
            else:
                tenant_response_content = tenant_response.text
        else:
            # json format
            if str(output_type).lower() == 'json':
                tenant_response_content = tenant_response.json()
            # Response object
            elif str(output_type).lower() == 'response':
                tenant_response_content = tenant_response
            # raw text file
            else:
                tenant_response_content = tenant_response.text
            print(tenant_response_content)
    except:
        print('Cannot POST the content to ' + tenant_url)
        pass
    # return
    return tenant_response_content