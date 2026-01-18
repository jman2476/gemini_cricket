import os
from utility.validate_path import validate_path
from google.genai import types

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

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)