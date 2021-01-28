a = 2 ** 1000

ans = 0

for i in range(0, len(str(a))):
	ans += int(str(a)[i])
	
print(ans)

#ans: 1366