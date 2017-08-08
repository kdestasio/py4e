# Let the user choose the file name
fname = input('Enter the file name: ')
try :
    fhand = open(fname)
except :
	print('File cannot be openned:', fname)
	exit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

# Code: http://www.py4e.com/code3/search6.py