mylist = [1,2,3,4]
for item in mylist:
    #I can add a parameter to print that enables me to print in 1 line
    #in this case is a spaceso there are spaces between the items
    print(item, end=' ')
print('\n')
for item in mylist:
    #hello will be printed 4 times because that is the length of the list
    print('hello')

for letter in 'This is a string':
    print(letter)

for letter in 'This is a string':
    print('hello')

tup = (1,2,3,4)
for num in tup:
    print(num)

list_of_tups = [(1,2), (3,4), (5,6), (7,8), (9,10)]
for tup_item in list_of_tups:
    print(tup_item)

list_of_tups = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
#this is called tuple unpacking, i.e. unpacking the items of each tuple separately
for item1, item2 in list_of_tups:
    print(item1)
    print(item2)
    print('\n')

for num1,num2 in list_of_tups:
    print(num1)
print('\n')

d = {'a':1, 'b':2, 'c':3}
for item in d:
    #it only prints the keys
    #when using for with dictionaries it doesn't neccesarily print them in order
    print(item)
print('\n')

for item in d.keys():
    #this will only print the keys
    print(item)
print('\n')

for item in d.items():
    #this will print as pairs of tuples
    print(item)
print('\n')

for key,value in d.items():
    print(key)
    print(value)
print('\n')

for k in d:
    #print only the values
    print(d[k])
print('\n')

for letter in 'code':
    #if I want to ommit the printing of d I use the continue command
    if letter == 'd':
        continue
    print(letter)
print('\n')
