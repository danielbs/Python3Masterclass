#Character identifiers
#character  Description         Example_pattern_code    Example_match
#   \d          A digit             file_\d\d               file_25
#   \w          Alphanumeric        \w-\w\w\w               A-b_1
#   \s          white space         a\sb\sc                 a b c
#   \D          A non digit         \D\D\D                  ABC
#   \W          Non-alphanumeric    \W\W\W\W\W              *-+=)
#   \S          Non-whitespace      \S\S\S\S                YOYO

#Quantifiers
#character      Description                 Example_pattern_code    Example_match
#   +           Occurs one or more time     Version \w-\w+          Version A-b1_1
#   {3}         Occurs exactly 3 times      \D{3}                   abc
#   {2,4}       Ocurrs 2 to 4 times         \d{2,4}                 123
#   {3,}        Ocurrs 3 or more times      \w{3,}                  anycharacters
#   *           Ocuurs zero or more times   A*B*C*                    AAACC
#   ?           once or none                plurals?                plural

import re

text = 'My phone number is 408-555-1234'
phone = re.search('408-555-1234',text)
print(phone)
#the r indicates that this \d are regular expressions and not escape characters
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone)
print(phone.group())
