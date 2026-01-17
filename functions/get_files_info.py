import os
from utility.validate_path import validate_path
def get_files_info(working_directory, directory="."):
    try:
        valid_directory, target_dir = validate_path(working_directory, directory)
        
        if not os.path.isdir(target_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'
        if not valid_directory: 
            return f'Error: "{directory}" is not a directory'

        ls_target_dir = os.listdir(target_dir)
        result = ''
        for item in ls_target_dir:
            item_abs = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_abs)
            is_dir = os.path.isdir(item_abs)
            result += f'- {item}: file_size= {file_size} bytes, is_dir={is_dir}\n'
        return result
    except Exception as e:
        return f'Error: get_files_info {e}'

