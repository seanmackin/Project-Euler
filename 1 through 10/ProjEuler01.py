#using the sum formula for 1,2,3,..,n = n(n+1)/2, we can math out the answer

def f(n):
	return (n * (n + 1) / 2)
	
sumthing = 3 * f(333) + 5 * f(199) - 15 * f(66)

print(int(sumthing))

#ans: 233168