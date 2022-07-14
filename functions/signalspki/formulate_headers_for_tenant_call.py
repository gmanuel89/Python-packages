## Import libraries
import base64

## Formulate the headers for calling the tenant through the APIs
def formulate_headers_for_tenant_call(authentication_type='api-key', authentication_parameters={}) -> dict:
    """
    # Authentication type ('api key', 'bearer token', 'core session cookie', 'basic')
    if 'api' in authentication_type.lower():
        authentication_type = 'api-key'
    elif 'bearer' in authentication_type.lower() or 'token' in authentication_type.lower():
        authentication_type = 'bearer-token'
    elif 'core' in authentication_type.lower() or'session' in authentication_type.lower() or 'cookie' in authentication_type.lower():
        authentication_type = 'core-session-cookie'
    else:
        authentication_type = 'api-key'
    """
    # Initialise output
    headers_api_call = {}
    if authentication_type == 'api-key':
        api_key = authentication_parameters.get('api_key')
        headers_api_call = {'x-api-key': api_key}
    elif authentication_type == 'core-session-cookie':
        core_session_cookie_id = authentication_parameters.get('core_session_cookie_id')
        headers_api_call = {'Cookie': core_session_cookie_id}
    elif authentication_type == 'bearer-token':
        bearer_token_id = authentication_parameters.get('bearer_token_id')
        headers_api_call = {'Authorization': 'Bearer ' + str(bearer_token_id)}
    elif authentication_type == 'basic':
        authentication_string = str(authentication_parameters.get('snb_username') +':' + authentication_parameters.get('snb_password'))
        authentication_string_bytes = authentication_string.encode('ascii')
        base64_encoded_authentication_string = base64.b64encode(authentication_string_bytes).decode('utf-8')
        headers_api_call = {'Authorization': 'Basic ' + str(base64_encoded_authentication_string)}
    #print('Headers: ' + str(headers_api_call))
    return headers_api_call
