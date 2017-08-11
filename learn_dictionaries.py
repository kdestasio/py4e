# Creating a dictionary

eng2span = dict()
eng2span['one'] = 'uno' # One iput form
print(eng2span)

eng2span = {'one' : 'uno', 'two' : 'dos', 'three' : 'tres'} # Another input form
print(eng2span)

print(eng2span['two'])

print('There are', len(eng2span), 'keys in the dictionary.') # Get the number of key:value pairs

if 'one' in eng2span : # 'in' tells whether the item is a key in the dictionary
	print('True')
else :
	print('False')
if 'uno' in eng2span :
	print('True')
else :
	print('False')

vals = list(eng2span.values()) # Return the dictionary values as a list
if 'uno' in vals :
	print('True')
else :
	print('False')

