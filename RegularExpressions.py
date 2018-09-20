#import regular expressions library
import re

text = "The agent's phone number is 408-555-1234. Call soon!!"
pattern = 'phone'
print(re.search(pattern, text))
#<_sre.SRE_Match object; span=(12, 17), match='phone'> it starts at index 12 and ends at 17
pattern = 'Not in text'
match = re.search(pattern, text)
print(match)
#the search returns 'none' so it doesn't print a thing
pattern = 'phone'
match = re.search(pattern, text)
print(match.span())
print(match.start())
print(match.end())
text = 'my phone once, my phone twice'
match = re.search(pattern, text)
#search only returns the first span even there are two results
print(match)
#to find multiple spans we use the findall method
matches = re.findall('phone', text)
print(matches)
print(len(matches))
#to find all the matches we can use the iterator
#if i use the command print(match.group()) it prints the actual text that was found
for match in re.finditer('phone', text):
    print(match)
for match in re.finditer('phone', text):
    print(match.group())
