#gotta import our square root function

from math import sqrt

#this is a twist on binet's formula, taking every third term as those are the even ones (3 * n)

def f(n):
	x = (((1 + sqrt(5)) / 2) ** (3*n) - ((1 - sqrt(5)) / 2) ** (3*n)) / sqrt(5)
	return x

	
#a running sum 

evens_sum = 0

#for-loop to loop through the numbers, shouldn't take more than 13 runs

for i in range(13):
	if f(i) < 4000000:
		evens_sum += f(i)
	else: 
		print(int(evens_sum))
		

#ans: 4613732