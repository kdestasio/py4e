# Exercise 3: Encapsulate this code in a function named count, 
# and generalize it so that it accepts the string and the letter as arguments.

def count(word, letter) :
	count = 0
	for i in word :
		if i == letter :
			count = count + 1
	print(count)