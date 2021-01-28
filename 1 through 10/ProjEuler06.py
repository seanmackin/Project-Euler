#gotta find a = (1 + 2 + 3 + 4) ** 2 - b = (1 ** 2 + 2 ** 2 + ... 100 ** 2)

a = 0

for i in range (1,101):
	a += i

a = a ** 2

b = 0

for i in range(1,101):
	b += i ** 2
	
ans = a - b

print(ans)

#ans: 25164150



