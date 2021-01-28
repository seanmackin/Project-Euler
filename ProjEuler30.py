list = []

for i in range(1,1000000):
    key = len(str(i))
    sum_a = 0
    for j in range(0, key):
        sum_a += int(str(i)[j]) ** 5
    if sum_a == i:
        list.append(i)

print(list)

ans = sum(list) - 1
print(ans)

#4150, 4151, 54748, 92727, 93084, 194979
#ans: 443839
