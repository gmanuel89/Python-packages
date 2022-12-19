#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-19
#####

## Import libraries and functions
import requests
from signalspki.inventa.get_file_from_uid import get_file_content_from_uid

## Get files info in a Project
def get_files_in_project(signals_inventa_project_uid: int, signals_inventa_project_revision: int, signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> list[dict]:
    # Initialise output
    files_in_project = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Retrieve content
    try:
        signals_inventa_project_files_response = requests.get(signals_inventa_tenant_url + 'project-service/projects/' + str(signals_inventa_project_uid) + '/revisions/' + str(signals_inventa_project_revision) + '/files',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key})
        signals_inventa_project_files_response_content = signals_inventa_project_files_response.json()
        # For every file entry...
        for prjfile in signals_inventa_project_files_response_content:
            single_file_info = {}
            # infer the file type
            if prjfile.get('dataSource').get('dataSourceType') == 'delimited':
                if prjfile.get('dataSource').get('dataSourceInfo').get('delimiter') == ',':
                    file_type = 'csv'
                else: #TODO implement specific delimited file formats
                    file_type = 'csv'
            else:
                file_type = 'xlsx'
            single_file_info['filetype'] = file_type
            # Get and store other information
            single_file_info['filename'] = prjfile.get('filename')
            single_file_info['dataSetUid'] = prjfile.get('dataSetUid')
            single_file_info['projectRevisionUid'] = prjfile.get('projectRevisionUid')
            single_file_info['projectRevisionFileUid'] = prjfile.get('projectRevisionFileUid') # file UID
            single_file_info['fileContent'] = get_file_content_from_uid(signals_inventa_project_uid, signals_inventa_project_revision, prjfile.get('projectRevisionFileUid'), signals_inventa_tenant_url, signals_inventa_tenant_api_key)
            # Decode file content if not binary
            if file_type == 'csv' and single_file_info['fileContent'] is not None:
                single_file_info['fileContent'] = single_file_info['fileContent'].decode('utf-8-sig')
            # Append information to the final list
            files_in_project.append(single_file_info)
    except:
        pass
    # return
    return files_in_project