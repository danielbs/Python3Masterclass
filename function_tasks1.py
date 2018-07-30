def check_ten(num1,num2):
    if num1 + num2 == 10:
        return 'True'
    else:
        return 'False'
print(check_ten(5,5))
print(check_ten(4,3))

#teacher solution to check ten
def t_check_ten(num1,num2):
    return num1 + num2 == 10

def check_ten_sum(num1,num2):
    if num1 + num2 == 10:
        return 'True'
    else:
        return num1+num2
print(check_ten_sum(5,5))
print(check_ten_sum(4,3))

def first_upper(mystring):
    sres = list(mystring)
    sres = ''.join(sres[0])
    return sres.upper()
print(first_upper('hello'))

#teacher solution for first upper
def t_first_upper(mystring):
    return mystring[0].upper()

def last_two(mystring):
    ltres = list(mystring)
    if len(ltres) > 1:
        ltres = ''.join(ltres[len(ltres)-2] + ltres[len(ltres)-1])
        print(ltres)
    else:
        print('Error!!')
    return

last_two('abcd')
last_two('d')

#teacher solution for last_two
def t_last_two(mystring):
    if len(mystring) < 2:
        return 'Error'
    else:
        #return substring starting in the end -2 until the end of the string
        return mystring[-2:]

def seq_check(nums):
    #enums = enumerate(nums)
    x = 0
    res = False
    while x < len(nums)-2:
        if (nums[x] == 1) and (nums[x+1] == 2) and (nums[x+2] == 3):
            res = True
            break
        x += 1
    print(res)
    return
seq_check([1,2,3,4,5,6])
seq_check([3,2,1,2,1,2,2,3,2,1,3,2,1])

#teacher solution to seq check
def t_seq_check(nums):
    for i in range(len(nums)-2):
        if (nums[i] == 1) and (nums[i+1] == 2) and (nums[i+2] == 3):
            return True
    return False

def compare_len(s1,s2):
    print(abs(len(s1)-len(s2)))
    return
compare_len('aa','bb')
compare_len('zbcbhnd','sdas')

def sum_or_max(mylist):
    if len(mylist) %2 == 0:
        print(sum(mylist))
    else:
        print(max(mylist))
    return
sum_or_max([1,2,3])
sum_or_max([1,2,3,4,5,6])

def replace_and_switch(name):
    output = list(name)
    for i,letter in enumerate(name):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i]='x'
    ll = output[i]
    output[i] = output[0]
    output[0] = ll
    #join converts the list into a string
    output = ''.join(output)
    print(output)
    return
replace_and_switch('James')
replace_and_switch('Alfred')

#teacher solution to replace_and_switch
def t_replace_and_switch(name):
    output = list(name)
    for i,letter in enumerate(name):
        if letter.lower() in ['a','e','i','o','u']:
            output[i]='x'
        else:
            output[i]=letter
    last = output[-1]
    first = output[0]
    output[0] = last
    output[-1] = first
    return ''.join(output)
