#find the nth fibonacci number that's above 1000 digits

f_k = 1
f_m = 1
f_n = 0

n = 3

for i in range(1,10000000000):
	f_n = f_k + f_m
	if f_n > 10 ** 999:
		print(n)
		break
	f_k = f_m
	f_m = f_n
	n += 1
	
#ans: 4782