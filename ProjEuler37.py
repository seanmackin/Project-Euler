p_list = []

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == False:
            return False
    if n % 2 == 0:
        return False
    else:
        return True

def L_test(n):
    if is_prime(n):
        word = str(n)
        new_word = word[1:len(word)]
        n = int(new_word)
        if n < 10 and is_prime(n):
            return True
        elif n < 10:
            return False
        else:
            return L_test(n)
    else:
        return False

def R_test(n):
    if is_prime(n):
        word = str(n)
        new_word = word[0:len(word)-1]
        n = int(new_word)
        if n < 10 and is_prime(n):
            return True
        elif n < 10:
            return False
        else:
            return R_test(n)
    else:
        return False

for p in range(10,1000000):
    if L_test(p) and R_test(p):
        p_list.append(p)

    if len(p_list) > 10:
        print(p_list)
        break

sum = 0
for n in p_list:
    sum += n
print(sum)

#ans : 748317
