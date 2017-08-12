# The urllib

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
# Code: http://www.py4e.com/code3/urllib1.py

# Get data and count the frequency of each word in the file
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand :
	words = line.decode().split()
	for word in words :
		counts[word] = counts.get(word, 0) + 1
print(counts)