
# Exercise 2: Write a program to prompt for a file name, 
# and then read through the file and look for lines of the form:
# `X-DSPAM-Confidence:0.8475`
# When you encounter a line that starts with "X-DSPAM-Confidence:" 
# pull apart the line to extract the floating-point number on the line. 
# Count these lines and then compute the total of the spam confidence values 
# from these lines. When you reach the end of the file, print out 
# the average spam confidence.

# Read in the file
fname = input('Enter the file name:')
try :
	fhand = open(fname)
except :
	print('File cannot be openned:', fname)

count = 0
added = 0
for line in fhand :
	line = line.rstrip() 
	if line.startswith('X-DSPAM-Confidence:') : 
		count = count + 1
		colon = line.find(':')
		num = float(line[colon+1:])
		added = added + num
print(count,'spam confidence intervals.')
average = added / count
print('The average spam confidence value for', fname, 'is', average)
print('Success!')