mystring = 'Secret agents are super good at staying hidden.'
mylist = mystring.split()
print(mylist)
for word in mylist:
    if word[0] == 's' or word[0] == 'S':
        print(word)
print('\n')

for word in mylist:
    if len(word)%2 == 0:
        print(word)
print('\n')

mylist2 = [x[0] for x in mylist]
for letter in mylist2:
    print(letter)
print('\n')

complist1 = [x for x in range(0,11) if x%2==0]
print(complist1)
print('\n')

myrange = list(range(0,11,2))
print(myrange)
print('\n')

from random import randint
myrn = []
for x in range(0,10):
    rn = randint(0,100)
    myrn.append(rn)
print(myrn)
print('\n')

rnl = [randint(0,100) for x in range(0,10)]
print(rnl)
print('\n')

even = False
while not even:
    number = int(input('Please provide an even number: '))
    if number%2 == 0:
        even = True
print('Thank You!')
print('\n')
