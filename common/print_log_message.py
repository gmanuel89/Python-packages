## Import libraries
import datetime

## Function to write the debugging messages to the console with a date prefix
def print_log_message(debug_message: str) -> None:
    return print(str(datetime.datetime.now()) + ' : ' + debug_message)
