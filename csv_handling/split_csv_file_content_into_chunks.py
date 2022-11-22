### Import libraries
import math

### Function to split the original CSV file content into chunks (input can be either the number of 'lines' per chunk or the number of 'chunks' to obtain)
def split_csv_file_content_into_chunks(csv_file_content: list[list] | list[dict], mode = 'chunks', number_of_output_chunks = 2, number_of_lines_per_chunk = 10) -> list[list[str]] | list[list[dict]]:
    # Initialise output variable
    csv_file_content_split = []
    # If there is no CSV content or only one line
    if csv_file_content is None or len(csv_file_content) <= 1:
        return csv_file_content
    # If the format is a list of lists
    if csv_file_content is not None and isinstance(csv_file_content[0], list):
        # Store the header (to be placed at every csv)
        csv_header = csv_file_content[0]
        # The actual lines are beyond the header
        total_number_of_lines = len(csv_file_content) - 1
    # If the format is a list of dictionaries
    elif csv_file_content is not None and isinstance(csv_file_content[0], dict):
        # Store the header (to be placed at every csv)
        csv_header = list(csv_file_content[0].keys())
        # The actual lines are beyond the header
        total_number_of_lines = len(csv_file_content)
    else:
        return csv_file_content
    # Calculate the number of lines per chunks
    if mode == 'chunks':
        if number_of_output_chunks is None or number_of_output_chunks == 0: number_of_output_chunks = 1
        number_of_lines_per_chunk = math.ceil(total_number_of_lines / number_of_output_chunks)
    # Use the input number of lines per chunks
    else: # elif mode == 'lines':
        number_of_lines_per_chunk = number_of_lines_per_chunk
        if number_of_lines_per_chunk > total_number_of_lines: number_of_lines_per_chunk = total_number_of_lines
        # Calculate the number of chunks
        number_of_output_chunks = math.ceil(total_number_of_lines / number_of_lines_per_chunk)
    # Initialise index variables
    lower_index = None
    higher_index = None
    # Start cycling after the header
    for i in range(number_of_output_chunks):
        if lower_index is None:
            lower_index = 1
        else:
            lower_index = lower_index + number_of_lines_per_chunk
        if higher_index is None:
            higher_index = number_of_lines_per_chunk + 1
        else:
            higher_index = higher_index + number_of_lines_per_chunk
        # Do not go over the length of the file lines
        if higher_index >= total_number_of_lines + 1 : higher_index = total_number_of_lines + 1
        # Retrieve the lines to be put into the output
        output_lines = csv_file_content[lower_index:higher_index]
        # Break out if there are no more lines
        if len(output_lines) == 0: break
        # Add the chunk to the final output
        if csv_file_content is None and isinstance(csv_file_content[0], list):
            output_lines_with_header = output_lines
            output_lines_with_header.insert(0, csv_header)
        else:
            output_lines_with_header = output_lines
        csv_file_content_split.append(output_lines_with_header)
    # return
    return csv_file_content_split
