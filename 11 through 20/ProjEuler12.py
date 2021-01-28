def factors(n):
    m = n
    factor_list = [];
    k = 2
    for k in range(1,round(m ** 0.5)+1):
        if m % k == 0:
            factor_list.append(k)
            factor_list.append(m/k)
        k += 1
    return(len(factor_list))

flag = True
n = 0
while(flag == True):
    n += 1
    print("N=" + str(n))
    t_n = (n ** 2 + n) / 2
    print("T_n=" + str(t_n))
    a=factors(t_n)
    print("Fact" + str(a))
    if a > 500:
        print(n)
        flag = False
