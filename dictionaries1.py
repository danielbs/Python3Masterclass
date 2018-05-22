d = {'key1':'value1', 'key2':'value2'}
print(d['key1'])
#adding new item to the dictionary
d['new_key'] = 'new item'
print(d)
d = {'a':1, 'z':2}
#print(d)
d['new'] = 0
print(d)
d = {'k1':10, 'k2':'stringy', 'k3':[1,2,3], 'k4':{'inside':100}}
print(d['k1'])
print(d['k2'])
print(d['k3'])
print(d['k4'])
print(d['k4']['inside'])
code_names = {'obama':'renegade',
                'bush':'trailblazer',
                'reagan':'rawhide',
                'ford':'passkey'}
print(code_names['ford'])
print(code_names.keys())
print(code_names.values())
print(code_names.items())
