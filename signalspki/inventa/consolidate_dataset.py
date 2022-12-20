#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-20
#####

## Import libraries and functions
import datetime
from signalspki.inventa.get_files_info_in_dataset import get_files_info_in_dataset
from signalspki.inventa.get_dataset_name_from_uid import get_dataset_name_from_uid
from signalspki.inventa.upload_csv_content_to_dataset import upload_csv_content_to_dataset
from signalspki.inventa.delete_files_from_project import delete_files_from_project
from csv_handling.read_csv_file_content import read_csv_file_content
from csv_handling.write_csv_file_content import write_csv_file_content

## Consolidate the files in one Inventa dataset in one single file
def consolidate_dataset(project_uid: int, dataset_uid: int, tenant_url: str, api_key: str) -> bool:
    # Initialise output
    operation_successful = False
    # Retrieve the list of file UIDs for the dataset
    files_in_dataset = get_files_info_in_dataset(project_uid, 0, dataset_uid, tenant_url, api_key)
    # Merge them in one single file (only if there is more than one file)
    if len(files_in_dataset) > 1:
        merged_file_content_rows = []
        total_number_of_rows = 0
        file_uid_list = []
        for f in files_in_dataset:
            # CSV
            if f.get('filetype') == 'csv':
                csv_content = read_csv_file_content(f.get('fileContent'), 'dictionary')
                total_number_of_rows = total_number_of_rows + len(csv_content)
                merged_file_content_rows.extend(csv_content)
                file_uid_list.append(f.get('projectRevisionFileUid'))
            else:
                # TODO implement other kinds of files...
                pass
        # Compare the new single file with the original files
        if (len(merged_file_content_rows) == total_number_of_rows) and total_number_of_rows > 0:
            # Write the CSV file content to a string
            merged_file_content_string = write_csv_file_content(merged_file_content_rows)
            # Upload the new file (retrieve the dataset name for the name of the new entry)
            dataset_name = get_dataset_name_from_uid(dataset_uid, project_uid, 0, tenant_url, api_key)
            file_upload_response = upload_csv_content_to_dataset(merged_file_content_string, dataset_name + '_merged_' + str(datetime.datetime.now()), project_uid, dataset_uid, tenant_url, api_key)
            if file_upload_response is not None and file_upload_response.ok:
                # Delete the old files (if upload successful)
                file_deletion_responses = delete_files_from_project(project_uid, 0, file_uid_list, tenant_url, api_key)
                # Determine if everything was successful
                if file_deletion_responses:
                    for resp in file_deletion_responses.keys():
                        if file_deletion_responses.get(resp).ok:
                            operation_successful = True
                        else:
                            operation_successful = False
                else:
                    operation_successful = False
    # return
    return operation_successful


