# Toy code to illustrate conditional steps

print('Script 1')
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')

print('')
print('Script 2')
if x > 2 :
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All done')