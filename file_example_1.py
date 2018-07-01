with open('test_file.txt') as my_file:
    lines = my_file.read()
    print(lines)

with open('test_file.txt') as my_file_lines:
    rlines = my_file_lines.readlines()
    print(rlines)
