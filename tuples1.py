mytuple = (1,2,3)
print(type(mytuple))
t = ('a', 1, 3.4)
print(t[0])
mylist = [1,2,3]
print(type(mylist))
mylist[0] = 'New'
print(mylist)
#mytuple[0] = 'New' will give an error because the tuple values can not be changed after initial value assigned
#a tuple has only 2 methods index and count
t = ('a', 'b', 'c', 'd', 'a')
print(t.index('b'))
print(t.count('a'))
