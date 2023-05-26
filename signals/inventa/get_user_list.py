#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-12-28
#####

## Import libraries
import requests

## Get list of users from tenant
def get_user_list(tenant_url: str, tenant_api_key: str) -> list[str]:
    # Initialise output
    user_list = []
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
        for u in users:
            user_list.append(u.get('userName'))
    except:
        pass
    # return
    return user_list