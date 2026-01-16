import os
from config import MAX_CHAR

def get_file_content(working_directory, file_path):
    try:
        # Validate path
        absolute_wd = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_wd, file_path))
        validate = os.path.commonpath([absolute_wd, target_file]) == absolute_wd
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
        return f'Error: {e}'
