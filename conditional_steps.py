# Toy code to illustrate conditional steps

print('Is x smaller than 10?')
x = input('What value should x have?\n')
x = int(x)

if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

#########
print('')
#########

print('Is x bigger than 2?')
x = input('What value should x have?\n')
x = int(x)

if x > 2 :
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

#########
print('')
#########

print('Are numbers in range x greater than 2?')
x = input('What value should x have?\n')
x = int(x)

for i in range(x) :
    print(i)
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All done')