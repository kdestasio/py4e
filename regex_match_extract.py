# Matching and extracting data with regex

import re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # Extract all the strings that match the pattern with findall
print(y)
y = re.findall('[AEIOU]+',x)

# Find all lines with email addresses
# Code: http://www.py4e.com/code3/re05.py
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)
 
# Search for lines that have an at sign between characters
# Code: http://www.py4e.com/code3/re06.py
hand = open('mbox-short.txt')
for line in hand : 
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]+', line)
    if len(x) > 0 :
    	print(x)


# Combining searching and extracting
# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
# Code: http://www.py4e.com/code3/re10.py
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
# Code: http://www.py4e.com/code3/re11.py

import re
hand = open('mbox-short.txt')
for line in hand : 
	line = line.rstrip()
	x = re.findall('^X\S*: ([0-9.]+)', line)
	if len(x) > 0 :
		print(x)