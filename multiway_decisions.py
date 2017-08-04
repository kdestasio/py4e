print('Is x smaller than 2 , greater than 10, or somewhere between?')
x = input('What value should x have?\n')
x = int(x)

if x < 2 :
	print('small')
elif x < 10 :
	print('Medium')
else :
	print('LARGE')
print('All done')