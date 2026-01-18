from functions.run_python_file import run_python_file

tests = [
    ['calculator', 'main.py', []],
    ['calculator', 'main.py', ['3 + 5']],
    ['calculator', 'tests.py'],
    ['calculator', '../main.py'],
    ['calculator', 'nonexistent.py'],
    ['calculator', 'lorem.txt'],
]

def main():
    for test in tests:
        print(f'Result for test: {test}')
        result = run_python_file(*test)
        print(result, '\n')

main()