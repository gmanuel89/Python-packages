#####
# Author: Manuel Galli
# e-mail: gmanuel89@gmail.com / manuel.galli@perkinelmer.com
# Updated date: 2022-10-07
#####

## Import libraries and functions
from signalspki.common.post_response_content_from_tenant import post_response_content_from_tenant
import csv
import tempfile

## Get list of entities from tenant
def get_signals_inventa_measurement_type_list(signals_inventa_tenant_url: str, signals_inventa_tenant_authentication: dict) -> list[str]:
    # Initialise output
    measurement_type_list = []
    # Call the API (generate an export CSV from the Inventa tenant, save it in memory and parse the MTYPE column)
    signals_inventa_measurement_type_list_response_content = post_response_content_from_tenant(signals_inventa_tenant_url, '/information-design-service/export', signals_inventa_tenant_authentication, payload_for_post_request={}, output_type='text')
    # generate temp file and write the csv content (coming from the tenant) into it
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf8', delete=False) as temporary_csv_file:
        temporary_csv_file.writelines(signals_inventa_measurement_type_list_response_content)
        # re-open the temporary csv file and read it as a normal csv
        with open(temporary_csv_file.name, 'r', encoding='utf8') as tmpfile:
            signals_inventa_measurement_type_list_csv_content = csv.DictReader(tmpfile)
            # extract the list of measurements
            for row in signals_inventa_measurement_type_list_csv_content:
                measurement_type_list.append(dict(row)['mtype||name'])
    # Extract the unique values
    measurement_type_list = list(set(measurement_type_list))
    # Discard the empty values
    measurement_type_list.remove('')
    # return
    return measurement_type_list