from functions.get_files_info import get_files_info

# Test format: [working_dir, directory]
tests = [
            ['calculator','.'],
            ['calculator', 'pkg'],
            ['calculator', '/bin'],
            ['calculator', '../']
        ]

def main():
    for test in tests:
        print(f'Result for "{test[1]}" directory:')
        result = get_files_info(*test)
        if 'Error:' in result:
            print(f'    {result}')
        else:
            res_list = result.split('\n')
            for res in res_list:
                print(f'    {res}')
main()
