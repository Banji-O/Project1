
# DICTIONARY

# Dictionary is also known as maps, hashtable, associate arrays -
# it stores keys and values
# Values are accessed using keys and not index

directory = {'Joe': 36366337, 'Rob': 3633636553, 'Tom': 77733929}

print(type(directory))

print('Tom\'s telephone number is: ',directory['Tom'])

# adding an item to dictionry

directory['Sam'] = 88777535

print(directory)

# deleting an item
del directory['Sam']
print(directory)

for key, values in directory.items():
    print('Key :', key, ' - Values :', values)

for key in directory:
    print('\nkey:', key, 'value:', directory[key])

print('Banji' in directory)

print(directory.clear())