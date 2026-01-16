from functions.get_file_content import get_file_content

tests = [
    ['calculator', 'lorem.txt'],
    ['calculator', 'main.py'],
    ['calculator', 'pkg/calculator.py'],
    ['calculator', '/bin/cat'],
    ['calculator', 'pkg/does_not_exist.py'],
]

def main():
    for test in tests:
        print(f'Result for file "{test[1]}":\n')
        result = get_file_content(*test)
        print(f'{result}')

main()