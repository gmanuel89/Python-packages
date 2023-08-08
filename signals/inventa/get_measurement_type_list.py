#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@revvity.com
# Updated date: 2022-12-06
#####

## Import libraries
import requests, csv, json, io

## Get list of measurements from tenant
def get_measurement_type_list(signals_inventa_tenant_url: str, signals_inventa_tenant_api_key: str) -> list[str]:
    # Initialise output
    measurement_type_list = []
    # Fix tenant URL
    if not signals_inventa_tenant_url.endswith('/'):
        signals_inventa_tenant_url = signals_inventa_tenant_url + '/'
    # Call the API (generate an export CSV from the Inventa tenant, save it in memory and parse the MTYPE column)
    try:
        signals_inventa_measurement_type_list_response = requests.post(signals_inventa_tenant_url + 'information-design-service/export',
                                                                    headers={'x-api-key': signals_inventa_tenant_api_key},
                                                                    data=json.dumps({})
                                                                    )
        signals_inventa_measurement_type_list_response_content = signals_inventa_measurement_type_list_response.text
        signals_inventa_measurement_type_list_csv_content = csv.DictReader(io.StringIO(signals_inventa_measurement_type_list_response_content))
        # extract the list of measurements
        for row in signals_inventa_measurement_type_list_csv_content:
            mtype_name = dict(row)['mtype||name']
            if mtype_name != '':
                measurement_type_list.append(mtype_name)
        # Extract the unique values
        measurement_type_list = list(set(measurement_type_list))
        # Sort alphabetically
        measurement_type_list.sort()
    except:
        pass
    # return
    return measurement_type_list