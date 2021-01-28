def primeFactorize(n):
	
	prime_factorization = []
	
	m = n
	
	while m > 1:
		
		for i in range(2, m + 1):
		
			if m % i == 0:
			
				prime_factorization.append(i)
			
				m = int(m / i)
				
				break
				
			if i > n / 2:
			
				return(prime_factorization)
			
				break
				
	if m == 1:
		
		return(prime_factorization)