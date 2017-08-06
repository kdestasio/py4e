# Breaking out of a loop

## Break - skips out of the loop
while True :
	line = input('> ')
	if line == 'done' :
		break
	print(line)

print('Done!')

## Continue- skips to the top of the loop
while True :
	line = input('> ')
	if line[0] == '#' :
		continue 
	if line == 'done' :
		break
	print(line)

print('Done!')