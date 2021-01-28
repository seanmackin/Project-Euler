input()

prime_list = []

def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    c = 0
    for p in range(2, n):
        if prime[p]:
            c += 1
            prime_list.append(p)

SieveOfEratosthenes(1000000)

print(prime_list)

def rotate(n):
    key = len(str(n))
    c = 1
    rotate_list = []
    rotate_list.append(n)
    r = str(n)
    while c < key:
        r = r + r[0]
        r = r[1:key+1]
        rotate_list.append(int(r))
        c += 1
    return(rotate_list)

rotate(12345)

for i in prime_list:
    for n in rotate(i):
        print(rotate(i))
        if n in prime_list:
                pass
        else:
            for k in rotate(i):
                if k in prime_list and len(str(k)) == len(str(n)):
                    prime_list = [x for x in prime_list if x!=k]


print(prime_list)
print(len(prime_list))
input()

#ans: 55
