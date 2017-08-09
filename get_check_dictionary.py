# The `get` method for dictionaries checks if a key 
# is already in a dictionary without a traceback

print('Running script 1')
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqain', 'cwen']
for name in names :
	if name not in counts :
		counts[name] = 1
	else :
		counts[name] = counts[name] + 1
	
	if name in counts: 
		x = counts[name]
		print(x, 'occurance(s) of', name)
	else :
	    x = 0
	x = counts.get(name, 0) # Default value if key does not exist

print('Total counts:', counts)


# Does the same thing as first 'if-then-else' loop in above cod, 
# but simplifies with get()

print('\nRunnig script 2')
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqain', 'cwen']
for name in names :
	counts[name] = counts.get(name, 0) + 1
print(counts)