import os
from utility.validate_path import validate_path
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        validate, target_file, cwd = validate_path(
            working_directory, file_path, ret_safe_dir=True)

        if args and '-f' in args:
            return 'Error: the force flag "-f" is not allowed for security'
        if not validate:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if '.py' not in target_file[-3:]:
            return f'Error: "{file_path}" is not a Python file'
        
        command = ['python', target_file]
        if args:
            command.extend(args)

        result = subprocess.run(
            command, 
            cwd=cwd, 
            timeout=30, 
            capture_output=True, 
            text=True
            )

        output = ''

        if result.returncode() != 0:
            output += f'Process exited with code {result.returncode} \n'
        if not result.stdout and not result.stderr:
            output += 'No output produced'
        if result.stdout:
            output += f'STDOUT: {result.stdout}\n'
        if result.stderr:
            output += f'STDERR: {result.stderr}'
        return output
    except Exception as e:
        return f'Error: executing python file: {e}'