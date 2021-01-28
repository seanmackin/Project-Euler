#run up to two million with a prime test on running primes, appending the primes and summing them as we go (starting with two)

primes = [2]

running_sum = 2

for i in range(3,2000000):

	tempcount = 0
	
	for j in primes:
			
		if i % j != 0:
				
			tempcount += 1
			
			if tempcount == len(primes):
			
				primes.append(i)
				
				running_sum += i
			
				print(running_sum)
		else:

			break
			
print(running_sum)

#lmao took hours oh well

#ans: 142913828922

