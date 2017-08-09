# Parsing mail data
fhand = open('mbox-short.txt') # open the file
for line in fhand :
	line = line.rstrip() # strip the whitespace off the right-hand side
	if not line startswith('From ') : continue # look for the matching string
	words = line.split() # split the line into component words
	print(words[2]) # word sub 2 is always the day of the week


# The double split pattern
fhand = open('mbox-short.txt') # open the file
for line in fhand :
	line = line.rstrip() # strip the whitespace off the right-hand side
	if not line startswith('From ') : continue # look for the matching string
	words = line.split()
	email = words[1] # Pull out the email address from the second position
	

fhand = open('mbox-short.txt') # open the file
for line in fhand :
	line = line.rstrip() # strip the whitespace off the right-hand side
	if not line startswith('From ') : continue # look for the matching string
	word = line.split()
	email = words[1]
	pieces = email.split('@')
	print(pieces[1])