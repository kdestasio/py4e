# Exercise 1: Write a program to read through a file and print the contents 
# of the file (line by line) all in upper case. 

fhand = open('mbox-short.txt')
count = 0
for line in fhand :
	line = line.rstrip().upper()
	print(line)