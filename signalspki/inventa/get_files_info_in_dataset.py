#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-22
#####

## Import libraries
import requests

## Get files info in a Dataset
def get_files_info_in_dataset(project_uid: int, project_revision: int, dataset_uid: int, tenant_url: str, tenant_api_key: str) -> list[dict]:
    # Initialise output
    files_info_in_dataset = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Fix project revision
    if project_revision is None:
        project_revision = 0
    # Retrieve the list of files for the project
    try:
        signals_inventa_project_files_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/files',
                                                            headers={'x-api-key': tenant_api_key})
        signals_inventa_project_files_response_content = signals_inventa_project_files_response.json()
        # For every file entry...
        files_in_project = []
        for prjfile in signals_inventa_project_files_response_content:
            single_file_info = {}
            # Get and store other information
            single_file_info['filename'] = prjfile.get('filename')
            single_file_info['dataSourceType'] = prjfile.get('dataSource').get('dataSourceType')
            single_file_info['dataSetUid'] = prjfile.get('dataSetUid')
            single_file_info['projectRevisionUid'] = prjfile.get('projectRevisionUid')
            single_file_info['projectRevisionFileUid'] = prjfile.get('projectRevisionFileUid') # file UID
            # Retrieve file content from UID
            try:
                project_file_response = requests.get(tenant_url + 'export-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/files/' + str(prjfile.get('projectRevisionFileUid')) + '/download',
                                                    headers={'x-api-key': tenant_api_key})
                file_content = project_file_response.content
            except:
                file_content = None
            single_file_info['fileContent'] = file_content
            # Decode file content if not binary
            if single_file_info['dataSourceType'] == 'delimited' and single_file_info['fileContent'] is not None:
                single_file_info['fileContent'] = single_file_info['fileContent'].decode('utf-8-sig')
            # Append information to the final list
            files_in_project.append(single_file_info)
    except:
        files_in_project = []
    # Get the files for that dataset
    for f in files_in_project:
        if f.get('dataSetUid') == dataset_uid:
            files_info_in_dataset.append(f)
    # return
    return files_info_in_dataset