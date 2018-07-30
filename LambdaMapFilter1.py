def square(num):
    return num**2
my_nums = [1,2,3,4,5]
#map(function,list) => creates a new list in which function runs on every item 
#of the original list and puts the result in the new list
for item in map(square,my_nums):
    print(item)
sq_nums = list(map(square,my_nums))
print(sq_nums)

def splicer(mystring):
    if len(mystring)%2==0:
        return 'even'
    else:
        return mystring[0]
mynames = ['A','BB','CCC','DDDD']
print(list(map(splicer,mynames)))

#filter is like map but only puts in the list elements that are boolean True
def check_even(num):
    return num%2==0
nums = [1,2,3,4,5,6]
e_nums = list(filter(check_even,nums))
print(e_nums)

#lambda expression
def nsquare(num):
    return num**2
#we can write this as follows
def lsquare(num): return num**2
#this is a lambda expression
lambda num: num**2
#this can be used a one time function in a map or filter
print(list(map(lambda x:x**2,[1,2,3])))
print(list(filter(lambda y:y%2==0,[1,2,3,4,5])))

#lambda that returns the first character in a string
#lambda s:s[0]
#lambda that returns the last character in a string
#lambda s:s[::-1]
#lambda that takes 2 params
#lambda x,y:x+y
