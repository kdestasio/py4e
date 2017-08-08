# Search through a file to find lines that start with 'From:'
fhand = open('mbox.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
		# Code: http://www.py4e.com/code3/search1.py


# Find lines that start with 'From:' and stip the white space
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
		# Code: http://www.py4e.com/code3/search2.py


# Skip lines that don't start with 'From:'
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
         # skip back to the beginning of the loop
    # Process our 'interesting' line
        print(line)
	# Code: http://www.py4e.com/code3/search3.py


# Find lines that contain the string `@uct.ac.za`
fhand = open('mbox.txt')
for line in fhand :
	line = line.rstrip()
	if line.find('@uct.ac.za') == -1 : continue
	print(line)
	# Code: http://www.py4e.com/code3/search4.py