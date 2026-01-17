import os
from config import MAX_CHAR
from utility.validate_path import validate_path

def get_file_content(working_directory, file_path):
    try:
        validate, target_file = validate_path(working_directory, file_path)
        
        if not validate:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Open and read file
        with open(target_file, 'r') as file: # reads file at file_path
            content = file.read(MAX_CHAR)
            if file.read(1): # try reading one more character
                content += f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
            return content
    except Exception as e:
        return f'Error: get_file_content {e}'
