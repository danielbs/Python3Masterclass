#basic function definition
def name_of_function():
    '''
    Docstring explains function
    '''
    print('Hello')
name_of_function()

def name_of_function_param(name):
    '''
    Docstring explains function
    '''
    print('Hello ' + name)
name_of_function_param('Daniel')

def add_function(param1, param2):
    return (param1+param2)
result = add_function(2,3)
print(result)

def report(name):
    print('Reporting {}'.format(name))
report('Jason')

def report2(name = 'Steve' ):
    print('Reporting {}'.format(name))
report2()

def report3(name = 'Steve' ):
    print('Reporting {}'.format(name))
report3('Sally')

def secret_check(mystring):
    return 'secret' in mystring.lower()
print(secret_check('This is a Secret'))

def code_maker(mystring):
    '''
    IN: is a string
    OUT: same string, but all vowels are convered to an x
    '''
    output = list(mystring)
    for i,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i]='x'
    

    return output