# Read in a file and count the lines

fhand = open('mbox.txt')
count = 0
for line in fhand :
	count = count + 1
print('Line Count:', count)

# Code: http://www.py4e.com/code3/open.py

# Read in a file all at once, print the file length and print the first 20 characters of the string data
# Only use read if the data can be easily stored in the computer's memory
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])