x = 0
while x < 3:
    print('X is currently:')
    print(x)
    print('Still less than 3, add 1 to X')
    x = x + 1
    print('\n')

print('Welcome Agent')
passcode = 0
while passcode != 123:
    #int is for casting the string input to an integer      
    #str is for casting a variable in to a string
    passcode = int(input('Please enter your passcode: '))
    if passcode != 123:
        print('Wrong password')
        print('Please try again')
        print('\n')
print('Correct passcode')

x = 0
while x < 10:
    x = x + 1
    print(x)
    if x == 3:
        break
