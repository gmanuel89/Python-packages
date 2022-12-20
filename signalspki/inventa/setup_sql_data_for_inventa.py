#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.inventa.get_project_uid_from_name import get_project_uid_from_name
from signalspki.inventa.get_map_id_from_name import get_map_id_from_name
from signalspki.inventa.get_project_latest_revision_number import get_project_latest_revision_number
from signalspki.inventa.get_dataset_list_for_project import get_dataset_list_for_project
from signalspki.inventa.get_dataset_uid_from_name import get_dataset_uid_from_name
from signalspki.inventa.create_new_dataset_in_project import create_new_dataset_in_project
from signalspki.inventa.associate_map_with_dataset import associate_map_with_dataset
from signalspki.inventa.setup_sql_entry_in_dataset import setup_sql_entry_in_dataset

## Loads the dataset into Signals Inventa
def setup_sql_data_for_inventa(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str, input_signals_inventa_project_name: str, input_signals_inventa_dataset_name: str, input_signals_inventa_map_name: str, sql_query: str, input_data_name: str, signals_inventa_connection_name: str) -> dict:
    # Get the Project UID from its name
    project_uid = get_project_uid_from_name(input_signals_inventa_project_name, signals_inventa_tenant_url, signals_inventa_tenant_api_key)
    # Get Map ID
    map_id = get_map_id_from_name(input_signals_inventa_map_name, signals_inventa_tenant_url, signals_inventa_tenant_api_key)
    # Retrieve project latest revision
    project_latest_revision = get_project_latest_revision_number(project_uid, signals_inventa_tenant_url, signals_inventa_tenant_api_key)
    # Determine if a new dataset must be created
    project_dataset_list = get_dataset_list_for_project(project_uid, signals_inventa_tenant_url, signals_inventa_tenant_api_key, 0)
    if str(input_signals_inventa_dataset_name) in project_dataset_list:
        # Get Dataset ID
        dataset_uid = get_dataset_uid_from_name(input_signals_inventa_dataset_name, input_signals_inventa_project_name, project_latest_revision, signals_inventa_tenant_url, signals_inventa_tenant_api_key)
        pass
    else:
        # Create a new dataset (and retrieve its UID)
        dataset_creation_response = create_new_dataset_in_project(input_signals_inventa_dataset_name, project_uid, signals_inventa_tenant_url, signals_inventa_tenant_api_key)
        if dataset_creation_response is not None:
            dataset_uid = dataset_creation_response.get('uid')
            # Associate a map to the dataset
            dataset_map_association = associate_map_with_dataset(dataset_uid, map_id, project_uid, signals_inventa_tenant_url, signals_inventa_tenant_api_key)
    # Setup the SQL entry
    sql_setup_response = setup_sql_entry_in_dataset(sql_query, input_data_name, signals_inventa_connection_name, project_uid, dataset_uid, signals_inventa_tenant_url, signals_inventa_tenant_api_key)
    return sql_setup_response