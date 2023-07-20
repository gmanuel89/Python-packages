#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2023-01-11
#####

## Import libraries and functions
import requests
from signals.inventa.get_map_id_from_name import get_map_id_from_name
from signals.inventa.get_dataset_list_for_project import get_dataset_list_for_project
from signals.inventa.get_dataset_uid_from_name import get_dataset_uid_from_name
from signals.inventa.create_new_dataset_in_project import create_new_dataset_in_project
from signals.inventa.associate_map_with_dataset import associate_map_with_dataset
from signals.inventa.setup_sql_entry_in_dataset import setup_sql_entry_in_dataset

## Generates a SQL dataset entry into Signals Inventa
def setup_sql_data_for_inventa(tenant_url: str, tenant_api_key: str, project_uid: int, dataset_name: str, map_id: str, sql_query: str, input_data_name: str, connection_name: str) -> requests.Response:
    # Determine if a new dataset must be created
    project_dataset_list = get_dataset_list_for_project(project_uid, tenant_url, tenant_api_key, 0)
    if str(dataset_name) in project_dataset_list:
        # Get Dataset ID
        dataset_uid = get_dataset_uid_from_name(dataset_name, project_uid, 0, tenant_url, tenant_api_key)
        pass
    else:
        # Create a new dataset (and retrieve its UID)
        dataset_creation_response = create_new_dataset_in_project(dataset_name, project_uid, tenant_url, tenant_api_key)
        if dataset_creation_response is not None:
            dataset_uid = dataset_creation_response.json().get('uid')
            # Associate a map to the dataset
            dataset_map_association = associate_map_with_dataset(dataset_uid, map_id, project_uid, tenant_url, tenant_api_key)
        else:
            dataset_uid = None
    # Setup the SQL entry
    sql_setup_response = setup_sql_entry_in_dataset(sql_query, input_data_name, connection_name, project_uid, dataset_uid, tenant_url, tenant_api_key)
    return sql_setup_response
