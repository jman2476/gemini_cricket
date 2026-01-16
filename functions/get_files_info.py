import os

def get_files_info(working_directory, directory="."):
    try:
        absolute_wd = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_wd, directory))
        if not os.path.isdir(target_dir): raise Exception('not dir')

        # validate that LLM is operating within bounds of desired directory
        valid_target_dir = os.path.commonpath([absolute_wd, target_dir]) == absolute_wd
        if not valid_target_dir: raise Exception('dir access denied')

        ls_target_dir = os.listdir(target_dir)
        result = ''
        for item in ls_target_dir:
            item_abs = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_abs)
            is_dir = os.path.isdir(item_abs)
            result += f'- {item}: file_size= {file_size} bytes, is_dir={is_dir}\n'
        return result
    except Exception as e:
        if e.args[0] == 'dir access denied':
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'
        elif e.args[0] == 'not dir':
            return f'Error: "{directory}" is not a directory'
        else: return 'Error: Unknown error occured while listing directory'

