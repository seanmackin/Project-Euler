#gotta find a^2 + b^2 = c^2 where a + b + c = 1000. setting up some efficient ranges from basic inequalities and a test yields the answer quickly

#x = int(input("a + b + c = "))
x = 1000

for a in range(1, x + 1):

	for b in range(a + 1, x + 1 - a):

		c = x - a - b

		if a ** 2 + b ** 2 == c ** 2:

			print("%s, %s, %s" % (a,b,c))
			print(a * b * c)

			break

	if a == x:

		print("No such triple exists.")

#ans: (200, 375, 425) -> 31875000
