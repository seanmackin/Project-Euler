largest_chain_number = 0
largest_chain_count = 0

for n in range(1,1000001):
		m = n
		tempcount = 0
		while n != 1:
			if n % 2 == 0:
				n = n / 2
				tempcount += 1
			else:
				n = 3 * n + 1
				tempcount += 1
		if n == 1:
			if tempcount > largest_chain_count:
				print(largest_chain_number, largest_chain_count)
				largest_chain_number = m
				largest_chain_count = tempcount

print("b", largest_chain_number, largest_chain_count)

#ans: 837799
