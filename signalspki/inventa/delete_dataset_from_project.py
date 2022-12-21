#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-21
#####

## Import packages
import requests

## Deletes a dataset from an Inventa project
def delete_dataset_from_project(dataset_uid: int, project_uid: int, tenant_url: str, tenant_api_key: str) -> requests.Response | None:
    # Initialise output
    dataset_deletion_response = None
    # Trigger the dataset creation
    try:
        dataset_deletion_response = requests.delete(tenant_url + 'project-service/projects/' + str(project_uid) + '/datasets/' + str(dataset_uid),
                                                    headers={'x-api-key': tenant_api_key}
                                                    )
    except:
        pass
    # return
    return dataset_deletion_response
