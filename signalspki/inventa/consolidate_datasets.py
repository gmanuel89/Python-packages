#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2023-02-24
#####

## Import libraries and functions
import datetime
from signalspki.inventa.associate_map_with_dataset import associate_map_with_dataset
from signalspki.inventa.create_new_dataset_in_project import create_new_dataset_in_project
from signalspki.inventa.get_files_info_in_dataset import get_files_info_in_dataset
from signalspki.inventa.get_dataset_uid_from_name import get_dataset_uid_from_name
from signalspki.inventa.get_map_id_for_dataset import get_map_id_for_dataset
from signalspki.inventa.upload_csv_content_to_dataset import upload_csv_content_to_dataset
from signalspki.inventa.delete_dataset_from_project import delete_dataset_from_project
from csv_handling.read_csv_file_content import read_csv_file_content
from csv_handling.write_csv_file_content import write_csv_file_content

## Consolidate the files in all the Inventa datasets with the same name in one single file in a single dataset
def consolidate_datasets(project_uid: int, dataset_name: str, tenant_url: str, api_key: str) -> bool:
    # Initialise output
    operation_successful = False
    # Get the dataset UID
    dataset_uid_list = get_dataset_uid_from_name(dataset_name, project_uid, 0, tenant_url, api_key)
    # Retrieve the list of file UIDs for the datasets
    files_in_datasets = []
    for dt in dataset_uid_list:
        files_in_single_dataset = get_files_info_in_dataset(project_uid, 0, dt, tenant_url, api_key)
        files_in_datasets.extend(files_in_single_dataset)
    # Merge them in one single file (only if there is more than one file)
    if len(files_in_datasets) > 1:
        merged_file_content_rows = []
        total_number_of_rows = 0
        file_uid_list = []
        for f in files_in_datasets:
            # Delimited (CSV, TSV)
            if f.get('dataSourceType') == 'delimited':
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
            # Upload the new file (to a new dataset, retrieving the dataset map)
            map_id = get_map_id_for_dataset(dataset_uid_list[0], project_uid, 0, tenant_url, api_key)
            new_dataset_creation_response = create_new_dataset_in_project(dataset_name, project_uid, tenant_url, api_key)
            if new_dataset_creation_response.ok:
                new_dataset_uid = new_dataset_creation_response.json().get('uid')
                dataset_map_association = associate_map_with_dataset(new_dataset_uid, map_id, project_uid, tenant_url, api_key)
                if dataset_map_association.ok:
                    file_upload_response = upload_csv_content_to_dataset(merged_file_content_string, dataset_name + '_merged_' + str(datetime.datetime.now()), project_uid, new_dataset_uid, tenant_url, api_key)
                    if file_upload_response is not None and file_upload_response.ok:
                        # Delete the old datasets (if upload successful)
                        dataset_deletion_responses = {}
                        for dt in dataset_uid_list:
                            dataset_deletion_responses[dt] = delete_dataset_from_project(dt, project_uid, tenant_url, api_key)
                        # Determine if everything was successful
                        if dataset_deletion_responses:
                            for resp in dataset_deletion_responses.keys():
                                if dataset_deletion_responses.get(resp).ok:
                                    operation_successful = True
                                else:
                                    operation_successful = False
                        else:
                            operation_successful = False
    # return
    return operation_successful
