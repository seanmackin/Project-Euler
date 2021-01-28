
#gotta make a function to find the largest prime factor for a number n, then call it on the number (lpf)

def lpf(n):
	
	#setting up some dummy variables and a empty list of the prime factors
	
	prime_factors = [1]
	count = len(prime_factors)
	
	#using a forloop to cycle through the bottom half of numbers in n, as n/2 is the greatest factor beside itself (using n ** 2 can be faster but allows for error)
	
	for i in range(2, int(n / 2 + 1)):
	
		#here, if the number i divides n, we know it's a factor
		
		if n % i == 0:
		
			#now we gotta test if i is prime. so, if no j in the prime factors already divides i, this forloop yields a temporary count = to the # of prime factors
			
			tempcount = 0
			
			for j in prime_factors:
				if i % j == 0:
					tempcount += 1
			
			if count == tempcount:
				prime_factors.append(i)
	
	#if the only factor in the list is "1", we must append n itself as n is prime
	
	if prime_factors == [1]:
		prime_factors.append(n)
		
	#now, we have to pick the largest number from the list of prime factors
	
	print(prime_factors)
	print("The largest prime factor is " + str(max(prime_factors)) + ".")
	
x = input("What number would you like to evalute for its largest prime factor? ")

lpf(int(x))

#holy shit this function is slow for things greater than 10 million or so

#ans: 6857
