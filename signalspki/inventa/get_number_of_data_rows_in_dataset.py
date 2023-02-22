#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-02-22
#####

## Import libraries
import requests, io, csv

## Retrieves size of a dataset in a project (in terms of number of rows in the data)
def get_number_of_data_rows_in_dataset(tenant_url: str, tenant_api_key: str, project_uid: int, dataset_uid: int, project_revision=0) -> int | None:
    # Initialise output variable
    number_of_data_rows_in_dataset = 0
    # Fix tenant URL
    if not tenant_url.endswith('/'): tenant_url = tenant_url + '/'
    # Fix project revision
    if project_revision is None: project_revision = 0
    # Retrieve all the files for the specific dataset, read their content and calculate the number of rows
    try:
        # Retrieve the list of files for the project
        signals_inventa_project_files_response = requests.get(tenant_url + 'project-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/files',
                                                            headers={'x-api-key': tenant_api_key})
        signals_inventa_project_files_response_content = signals_inventa_project_files_response.json()
        # For every file entry...
        for project_file in signals_inventa_project_files_response_content:
            # Get and store other information
            dataSourceType = project_file.get('dataSource').get('dataSourceType')
            dataSetUid = project_file.get('dataSetUid')
            projectRevisionUid = project_file.get('projectRevisionUid')
            projectRevisionFileUid = project_file.get('projectRevisionFileUid') # file UID
            # Proceed only for the files that are in the desired dataset
            if dataSetUid == dataset_uid:
                # Retrieve file content from UID
                try:
                    project_file_response = requests.get(tenant_url + 'export-service/projects/' + str(project_uid) + '/revisions/' + str(project_revision) + '/files/' + str(projectRevisionFileUid) + '/download',
                                                        headers={'x-api-key': tenant_api_key})
                    file_content = project_file_response.content
                except:
                    file_content = None
                # Decode file content if not binary
                if dataSourceType == 'delimited' and file_content is not None:
                    file_content = file_content.decode('utf-8-sig')
                # Read the string file content and determine the number of rows
                file_content = io.StringIO(file_content)
                file_dictionary = csv.DictReader(file_content)
                file_lines = []
                for row in file_dictionary:
                    file_lines.append(dict(row))
                # Sum up the number
                number_of_data_rows_in_dataset = number_of_data_rows_in_dataset + len(file_lines)
    except:
        pass
    # return
    return number_of_data_rows_in_dataset



tenant_url = 'https://jnj-discovery-engine-sdf.sf.perkinelmercloud.com/'
tenant_api_key = '1h4202g2b59mi832g5da3051gpnndlulvlh5g5d6gp1jkluma9q8'
project_uid = 14
dataset_uid = 2372
number_of_data_rows = get_number_of_data_rows_in_dataset(tenant_url, tenant_api_key, project_uid, dataset_uid, 0)
print('Number of data rows for project UID %s: %s' %(project_uid, number_of_data_rows))
