N = []
primes = []

for i in range(2,3000):
    N.append(i)

cnt = 1
for i in N:
    cnt += 1
    if i != -1:
        for j in range(cnt,len(N)):
            k = N[j]
            if i != k:
                if k % i == 0:
                    N[j] = -1

for n in N:
    if n > 0:
        primes.append(n)

n_list = []

for i in range(500,1000):
    odd_n = 2*i + 1
    for j in range(500,1000):
        for p in primes:
            n = j + p
            if n <= odd_n:
                if n not in n_list[n:1000]:
                    n_list.append(n)


for i in range(500,1000):
    if (2*i+1) not in n_list:
        print(2*i+1)

print(primes)
