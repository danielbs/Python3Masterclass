#range allows me to define a list of integers
#range is a generator, it doesn't save all the included elements in memory
#in this case from 0 to 10, the 11 is not included
for num in range(0,11):
    print(num)
#in this case 2 is the step size like x=x+2
for num in range(0,11,2):
    print(num)
print(list(range(0,51,5)))

index = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index, letter))
    index += 1

#or we can do it using enumeration
#enumerate generates a list of tupples in which the first item is the index
for index,letter in enumerate('abcde'):
    print('At index {} the letter is {}'.format(index, letter))

print(list(enumerate('abcde')))

#zip ties together 2 lists to make a list of tupples
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
for item in zip(mylist1,mylist2):
    print(item)

#the in operator can be used outside of a for loop to check if some data is inside a list
print('x' in [1,2,3])
print('x' in ['a','b','x'])
print('x' in 'abcde')
print('x' in 'acx')

#min max operators
mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

#import function shuffle from random library
from random import shuffle
#shuffle is ussed to permanantely change a list item's order
shuffle(mylist)
print(mylist)

#randint generates a random integer between a range including the limits
from random import randint
print(randint(0,100))

#conditional operators
#x<y x>y x==y x!=y
#and or
#not reverse the boolean value that is given to it
