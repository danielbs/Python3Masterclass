#error_file = open('some_text.txt')
my_file = open('test_file.txt')
#this should print the contents of the file including \n without the line breaks, a long line
print(my_file.read())
print(my_file.read())
#the second print doesn't display nothing because the cursor is at the end of the file and there is nothing to display
#reset cursor to srart of file
my_file.seek(0)
print(my_file.read())
#print the file with lines because that includes \n
my_file.seek(0)
print(my_file.readlines())
my_file.close()

with open('test_file.txt') as my_file:
    lines = my_file.read()
print(lines)

#open second file in reading mode
f = open('second_file.txt', mode='r')
print(f.read())
f.close()

#'w' is the same as mode='w'
f = open('second_file.txt', 'w')
f.write('new line')
f.close()
#the print will show only new line because mode w rewrites the file with this content
with open ('second_file.txt') as f:
    print(f.read())

with open('stam.txt', 'w') as f:
    f.write('New file made')
with open('stam.txt', 'r') as f:
    print(f.read())
#mode a is append and a+ is append + read
with open('stam.txt', 'a') as f:
    #including \n to make the line break
    f.write('\nsome other line')
with open('stam.txt', 'r') as f:
    print(f.read())
