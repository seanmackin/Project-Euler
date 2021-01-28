#so we know the answer belongs in Z = [100,999] ** 2, in the integers (but is commutative), so we should make two loops, making a list of 900 ** 2 ordered pairs.

possible_products = []

for i in range(100,1000):
	for j in range(i,1000):
		possible_products.append(j*i)

print(possible_products)

#now we want to define a general palindrome test for an n

def palindrome_test(n):
	if n == int(str(n)[::-1]):
		return True
	else:
		return False

palindromes = []

#applying the test to all elements in the possible products list

for i in possible_products:
	if palindrome_test(i):
		palindromes.append(i)
		
print(palindromes)

print("The biggest possible palindrome is " + str(max(palindromes)))

#ans: 906609