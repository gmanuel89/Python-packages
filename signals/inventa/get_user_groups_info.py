#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-28
#####

## Import libraries
import requests

## Retrieves information about User Groups
def get_user_groups_info(tenant_url: str, tenant_api_key: str) -> list[dict]:
    # Initialise output
    user_groups_info = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Retrieve response from tenant
    try:
        user_groups_info_response = requests.get(tenant_url + 'sso-auth/api/userstore/sso-user-groups-mongo?sort=groupName',
                                                    headers={'x-api-key': tenant_api_key})
        user_groups_info_response_content = user_groups_info_response.json()
        # Retrieve the user group information specifically
        user_groups = user_groups_info_response_content.get('_embedded').get('sso-user-groups')
        user_groups_info = user_groups
    except:
        pass
    # return
    return user_groups_info
