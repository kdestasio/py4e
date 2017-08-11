# Tuples - unmodifiable lists with key:value pairs

(x, y) = (4, 'fred') # Assigning a tuple
print(x)
print(y)

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items() :
	print(k, v)

tups = d.items()
print(tups)

# Tuples are comparable
print('Is (0, 1, 2) < (5, 1, 2)?')
if (0, 1, 2) < (5, 1, 2) :
	print('True, because elements are evaluated pairwise from left to right')
else :
	print('False')

# Sorting lists of tuples
d = {'a':10, 'b':1, 'c':22}
d.items()
print('Sorting items in:', d)
t = sorted(d.items())
print(t)

# Using a loop to sort by key
for k, v in sorted(d.items()) : # Sort the dictionary in key order
	print(k,v)

# Sort by value
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
	tmp.append( (v, k) ) # tmp is a list, but each thing in the list is a tuple
print(tmp) # Print the values and keys, now reversed
tmp = sorted(tmp, reverse = True) # sort from high to low
print(tmp)

# Count values
fhand = open('romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
    	counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items() :
	newtup = (val, key) # make a tuple thats value:key
	lst.append(newtup)

lst = sorted(lst, reverse = True) # Sort value:key tuples from highest to lowest value
for val, key in lst[:10] : # Look for top 10 (values 0-10 in the list)
	print(key, val) # print as key:value pairs

# Even shorter version
fhand = open('romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
    	counts[word] = counts.get(word, 0) + 1

print( sorted( [ (v,k) for k,v in counts.items() ], reverse = True ) )
for val, key in lst[:10] : 
	print(key, val) 

