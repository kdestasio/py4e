# Convert Farenheit to Celsius

inp = input('Enter Farenheit Temperature: ')
try :
	fahr = float(inp)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print(cel)
except :
	print('Please print a number')

# Code: http://www.py4e.com/code3/fahren.py
# Code: http://www.py4e.com/code3/fahren2.py