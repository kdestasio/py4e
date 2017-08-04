print('Is x smaller than 2 , greater than 10, or somewhere between?')
x = input('What value should x have?\n')
x = int(x)

if x < 2 :
	print('small')
elif x < 10 : # Can have as many 'elif's as wanted
	print('Medium')
else : # If there is no 'else' it is possible that none will execute
	print('LARGE')
print('All done')