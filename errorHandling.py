try:
    1 + '2'
except TypeError:
    print('You are not adding the correct elements together')
else:
    print('Everything went somoothly')

try:
    result = input('Please enter a number: ')
    1 + int(result)
except ValueError:
    print('Please make sure to input a number')
else:
    print('Everything went somoothly')

#I dont have to specify what type of error to catch
try:
    result = input('Please enter a number: ')
    1 + int(result)
except:
    print('Hey, an error occured')
else:
    print('Everything went somoothly')

try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    print('Hey an error happened')
else:
    print('Everything worked')

#finally allows the code to continue although there was an error
#in case of an error the except code AND the finally code will run both
try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    print('Hey an error happened')
finally:
    print('Finally I run this block of code')
