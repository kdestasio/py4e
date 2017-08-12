# Regular expressions

import re

hand = open('mbox-short')
for line in hand :
	line = line.rstrip()
	if re.serach('^From:', line) :
		print(line)