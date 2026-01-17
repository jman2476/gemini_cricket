import os
from utility.validate_path import validate_path

def write_file(working_directory, file_path, content):
    try:
        # Validate path
        validate, target_file = validate_path(working_directory, file_path)
        if not validate: 
            return f'Error: Cannot write to "{file_path}" as it is outside permitted working directory'
        
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}": it is a directory'

        os.makedirs(file_path, exist_ok=True)
        
        with open(target_file, 'w') as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: write_file {e}'
