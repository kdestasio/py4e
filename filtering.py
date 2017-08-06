# Filtering in a loop

## Search integers
print('Searching for values greater than 20')
print('Before')
for value in [19, 41, 12, 3, 74, 15] :
	if value > 20 :
		print('Large number:', value)
print('Done')

## Search booleans
found = False
print('\nSearching for the number 3')
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
	if value == 3 :
		found = True
	print(found, value)
print('After', found)

## Search small values
print('\nSearching for values smaller than 20')
print('Before')
for value in [19, 41, 12, 3, 74, 15] :
	if value < 20 :
		print('Small number:', value)
print('Done')

## Search smallest values
print('\nSearching for the smallest number')
smallest = None
print('Before', smallest)
for value in [9, 41, 12, 3, 74, 13] :
	if smallest is None :
		smallest = value
	elif value < smallest :
		smallest = value
	print(smallest, value)
print('After', smallest)