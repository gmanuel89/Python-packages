#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-28
#####

## Import libraries
import requests

## Retrieves information about Users
def get_users_info(tenant_url: str, tenant_api_key: str) -> list[str]:
    # Initialise output
    users_info = []
    # Fix tenant URL
    if not tenant_url.endswith('/'):
        tenant_url = tenant_url + '/'
    # Call the API
    try:
        user_list_response = requests.get(tenant_url + 'sso-auth/api/userstore/sso-users-mongo?sort=groupName',
                                        headers={'x-api-key': tenant_api_key})
        user_list_response_content = user_list_response.json()
        # Retrieve the user information specifically
        users = user_list_response_content.get('_embedded').get('sso-users')
        users_info = users
    except:
        pass
    # return
    return users_info