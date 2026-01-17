from functions.write_files import write_file

tests = [
            ['calculator', 'lorem.txt', 'wait, this isn\'t lorem ipsum'],
            ['calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet'],
            ['calculator', '/tmp/temp.txt', 'this should not be allowed']
        ]


def main():
    for test in tests:
        print(f'Result for file {test[1]}:\n')
        result = write_file(*test)
        print(result)

main()
