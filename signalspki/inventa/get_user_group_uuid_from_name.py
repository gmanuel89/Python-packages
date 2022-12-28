#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-28
#####

## Import libraries
import requests

## Retrieves UUID from User Group
def get_user_group_uuid_from_name(user_group_name: str, tenant_url: str, tenant_api_key: str) -> str:
    # Initialise output
    user_group_uuid = None
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
        # Retrieve the UUID of the group
        for group in user_groups:
            if group.get('groupName') == user_group_name:
                user_group_uuid = group.get('uuid')
                break
    except:
        pass
    # return
    return user_group_uuid
