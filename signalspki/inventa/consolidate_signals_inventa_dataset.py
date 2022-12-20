## Import libraries and functions
import datetime
from signalspki.inventa.get_file_uids_for_dataset import get_file_uids_for_dataset
from signalspki.inventa.get_signals_inventa_dataset_name_from_uid import get_signals_inventa_dataset_name_from_uid
from signalspki.inventa.upload_csv_to_signals_inventa_dataset import upload_csv_to_signals_inventa_dataset
from signalspki.inventa.delete_files_from_signals_inventa_project import delete_files_from_signals_inventa_project
from csv_handling.read_csv_file_content import read_csv_file_content
from csv_handling.write_csv_file_content import write_csv_file_content

## Consolidate the files in one Inventa dataset in one single file
def consolidate_signals_inventa_dataset(signals_inventa_project_uid: int, signals_inventa_dataset_uid: int, signals_inventa_tenant_url: str, signals_inventa_api_key: str) -> bool:
    # Initialise output
    operation_successful = False
    # Retrieve the list of file UIDs for the dataset
    files_in_dataset = get_file_uids_for_dataset(signals_inventa_project_uid, signals_inventa_dataset_uid, signals_inventa_tenant_url, signals_inventa_api_key)
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
            dataset_name = get_signals_inventa_dataset_name_from_uid(signals_inventa_dataset_uid, signals_inventa_project_uid, signals_inventa_tenant_url, signals_inventa_api_key)
            file_upload_response = upload_csv_to_signals_inventa_dataset(merged_file_content_string, dataset_name + '_merged_' + str(datetime.datetime.now()), signals_inventa_project_uid, signals_inventa_dataset_uid, signals_inventa_tenant_url, signals_inventa_api_key)
            if file_upload_response is not None and file_upload_response.ok:
                # Delete the old files (if upload successful)
                file_deletion_responses = delete_files_from_signals_inventa_project(signals_inventa_project_uid, file_uid_list, signals_inventa_tenant_url, signals_inventa_api_key)
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


