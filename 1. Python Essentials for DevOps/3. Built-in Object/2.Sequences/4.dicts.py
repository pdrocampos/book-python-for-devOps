'''
You can create a dict object using the dict() constructor. With no arguments,
it cre‐ ates an empty dict. It takes a sequence of key/value pairs as an argument 
as well:
'''

map = dict()
print(type(map))
print(map)
kv_list = [['key-1', 'value-1'],['key-2', 'value-2']]
print(dict(kv_list))

'''
You can also create a dict directly using curly braces:
'''

map = {'key-1': 'value-1', 'key-2': 'value-2'}
print(map)

'''
You can access the value associated with a key using square bracket syntax:
'''

print(map['key-1'])
print(map['key-2'])

'''
You can use the same syntax to set a value. If the key is not in the dict,
 it adds as a new entry. If it already exists, the value changes to the new value:
'''

print(map)
map['key-3'] = 'value-3'
print(map)
map['key-1'] = 13
print(map)

'''
If you try to access a key that has not been defined in a dict, a KeyError exception will be thrown
'''

#print(map['key-4'])

'''
You can check to see if the key exists in a dict using the in syntax we saw with sequences.
 In the case of dicts, it checks for the existence of keys:
'''

if 'key-4' in map:
    print(map['key-4'])
else:
    print('Key-4 not there')

'''
A more intuitive solution is to use the get() method. If you have not defined a key in a 
dict, it returns a supplied default value. If you have not supplied a default value, it 
returns None
'''

print(map.get('key-4', 'default-value'))

"""
Use del to remove a key-value pair from a dict:
"""

del(map['key-1'])
print(map)

"""
The keys() method returns a dict_keys object with the dict’s keys. The values() method 
returns an dict_values object, and the items() method returns key-value pairs. This last 
method is useful for iterating through the contents of a dict:
"""

print(map.keys())
print(map.values())
for key, value in map.items():
    print(f"{key}: {value}")

'''
Similar to list comprehensions, dict comprehensions are one-line statements return‐ 
ing a dict by iterating through a sequence:
'''

letters = 'abcde'
cap_map = {x: x.upper() for x in letters}
print(cap_map['e'])
print(cap_map)