import os

def validate_path(safe_directory, request_path, ret_safe_dir=False):
    try:    
        absolute_safe_dir = os.path.abspath(safe_directory)
        request_target = os.path.normpath(
            os.path.join(absolute_safe_dir, request_path)
            )
        validate = os.path.commonpath(
            [absolute_safe_dir, request_target]) == absolute_safe_dir
        if ret_safe_dir:
            return validate, request_target, absolute_safe_dir
        return validate, request_target
    except Exception as e:
        return f'Error: Path validation error {e}'
