#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-02-23
#####

## Import libraries and functions
from signals.inventa.associate_map_with_dataset import associate_map_with_dataset
from signals.inventa.create_new_dataset_in_project import create_new_dataset_in_project
from signals.inventa.delete_dataset_from_project import delete_dataset_from_project
from signals.inventa.get_files_info_in_dataset import get_files_info_in_dataset
from signals.inventa.get_dataset_name_from_uid import get_dataset_name_from_uid
from signals.inventa.get_map_id_for_dataset import get_map_id_for_dataset
from signals.inventa.upload_csv_content_to_dataset import upload_csv_content_to_dataset
from csv_handling.read_csv_file_content import read_csv_file_content
from csv_handling.write_csv_file_content import write_csv_file_content
from csv_handling.split_csv_file_content_into_chunks import split_csv_file_content_into_chunks

## Split the Inventa dataset in multiple datasets (it creates the new datasets and then removes the old one)
def split_dataset(project_uid: int, dataset_uid: int, maximum_number_of_rows_per_dataset: int, tenant_url: str, api_key: str) -> bool:
    # Initialise outputs
    operation_successful = False
    file_upload_responses = {}
    # Retrieve the dataset name from UID
    dataset_name = get_dataset_name_from_uid(dataset_uid, project_uid, 0, tenant_url, api_key)
    # Get the map associated with the dataset
    map_id = get_map_id_for_dataset(dataset_uid, project_uid, 0, tenant_url, api_key)
    # Retrieve the list of file UIDs for the dataset
    files_in_dataset = get_files_info_in_dataset(project_uid, 0, dataset_uid, tenant_url, api_key)
    # Merge them in one single file (or just take the file)
    merged_file_content_rows = []
    file_uid_list = []
    for f in files_in_dataset:
        # Delimited (CSV, TSV)
        if f.get('dataSourceType') == 'delimited':
            csv_content = read_csv_file_content(f.get('fileContent'), 'dictionary')
            merged_file_content_rows.extend(csv_content)
            file_uid_list.append(f.get('projectRevisionFileUid'))
        else:
            # TODO implement other kinds of files...
            pass
    # Split the (merged) CSV content in chunks of X rows each
    merged_file_content_rows_split = split_csv_file_content_into_chunks(merged_file_content_rows, 0, maximum_number_of_rows_per_dataset)
    # Each file originated from the split will correspond to a dataset, with one file corresponding to the chunk in it
    for split_content_rows in merged_file_content_rows_split:
        # Create the new corresponding dataset
        new_dataset_creation_response = create_new_dataset_in_project(dataset_name, project_uid, tenant_url, api_key)
        # If successful, upload the file
        if new_dataset_creation_response.ok:
            # Retrieve the newly created dataset
            new_dataset_uid = new_dataset_creation_response.json().get('uid')
            # Associate the newly created dataset with the map
            dataset_map_association = associate_map_with_dataset(new_dataset_uid, map_id, project_uid, tenant_url, api_key)
            if dataset_map_association.ok:
                # Write the CSV file content to a string
                split_file_content_string = write_csv_file_content(split_content_rows)
                # Upload the CSV file content
                file_upload_response = upload_csv_content_to_dataset(split_file_content_string, dataset_name + '_split', project_uid, new_dataset_uid, tenant_url, api_key)
                # Store the response
                file_upload_responses[new_dataset_uid] = file_upload_response
    # Determine if everything was successful
    file_uploads_successful = False
    if file_upload_responses:
        for resp in file_upload_responses.keys():
            if file_upload_responses.get(resp).ok:
                file_uploads_successful = True
            else:
                file_uploads_successful = False
    else:
        file_uploads_successful = False
    # If all the files have been uploaded, delete the original dataset
    if file_uploads_successful:
        initial_dataset_deletion_response = delete_dataset_from_project(dataset_uid, project_uid, tenant_url, api_key)
        if initial_dataset_deletion_response is not None and initial_dataset_deletion_response.ok:
            operation_successful = True
        else:
            operation_successful = False
    else:
        operation_successful = False
    # return
    return operation_successful
