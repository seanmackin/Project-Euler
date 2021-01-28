#what is the 10001st prime? make a list, stop at 10001, max(list)

n = int(input("Select the nth prime you'd like (up to 10001): n = "))

print(n)

primes = [2]

#using desmos and the prime counting function, we can see that the 10001st prime happens around a hundred thousand, so lets leave an upper bound of 110,000

for i in range(3,110000):

	amt_o_primes = len(primes)
	
	if amt_o_primes < n:
	
		tempcount = 0
		
		for j in primes:
			if i % j != 0:
				tempcount += 1
				
		if tempcount == amt_o_primes:
			primes.append(i)
			
	if amt_o_primes == n:
		print(primes)
		print("The prime you are searching for is " + str(max(primes)))
		break

#pretty slow code - not my best work

#ans: 104743
