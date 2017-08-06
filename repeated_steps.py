# Repeated steps

n = input('Countdown from:\n')

try :
	n = int(n)
except :
	print('Error: input is non-numeric')

while n > 0 :
	print(n)
	n = n - 1
print(n)
print('Blastoff!')