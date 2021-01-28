#using the permutation formula for ways to arrange objects, we see that this path is just a different collection of orderings of 20 rights and downs, thus

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
		
ans = factorial(40) / ( factorial(20) ** 2)
 
print(int(ans))

#ans: 137846528820