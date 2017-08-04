# Code that will not run
astr = 'Hello Krista'
try:
	istr = int(astr) # 'dangerous' line
except: # like an else, but is code that python will execute if something goes wrong
    istr = -1

print('First', istr)

# Code that will run
astr = '123'
try :
	istr = int(astr) 
except: 
	istr = -1

print('Second', istr)
