score = input("Enter Score: ")
try :
	score = float(score)
except :
	print('Error: non-numeric')
	quit()

if score > 1 :
    print('Error: score is out of range')
else :
    if score < 0 :
        print('Error: score is out of range')
    else :
        if  score >= 0.9 :
            print('A')
        elif score >= 0.8 :
            print('B')
        elif score >= 0.7 :
            print('C')
        elif score >= 0.6 :
            print('D')
        elif score < 0.6 :
            print('F')
