#sum up the digits of 100!
n = 1
for i in range (1,101):
    n *= i

sum = 0
for i in str(n):
    sum += int(i)

print(n)
print(sum)
#ans: 648
