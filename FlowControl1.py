if 1<2:
    print('condition met')
if 1 > 2:
    #boolean result false so it doesn't print 
    print('condition met')
cond = 1<2
if cond:
    print('cond met')
if 1==1:
    print('Condition met 1 = 1')
else:
    print('Last block happened to run')
if 2 == 0:
    print('first condition true')
elif 2 == 1:
    print('second condition true')
elif 2 == 2:
    print('third condition true')
else:
    print('nothing above was true')

#here the output will be second condition true because it is the first 
#boolean to be true, python exists the block without checking further
if 2 == 0:
    print('first condition true')
elif 2 == 2:
    print('second condition true')
elif 2 == 2:
    print('third condition true')
else:
    print('nothing above was true')

agent_code = 12345
access = False
if agent_code == 12345:
    print('Code Reset')
    print('Call a supervisor')
elif agent_code == 432234:
    print('Welcome agent 423234')
    access = True
else:
    print('Sorry not matching code')

######
######

if access:
    print('Access Granted')
else:
    print('Access Denied')
