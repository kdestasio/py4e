# Count letters and put them in a dictionary
word = input('Type a word: ')
d = dict()
for c in word :
	if c not in d : 
		d[c] = 1
	else :
		d[c] = d[c] + 1
print(d)

