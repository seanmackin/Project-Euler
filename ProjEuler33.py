for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):

            a = int(str(i) + str(k)) / int(str(j) + str(k))
            b = int(str(k) + str(i)) / int(str(j) + str(k))
            c = int(str(i) + str(k)) / int(str(k) + str(j))
            d = int(str(k) + str(i)) / int(str(k) + str(j))

            for frac in (a,b,c,d):
                if frac == i/j and frac < 1:
                    print(frac)
                    print(str(i) + str(j) + str(k))

#yields 146, 256, 159, 489
# we can then deduce that these fractions are 16/64 = 1/4, 26/65 = 2/5, 19/95 = 1/5, 49/98 = 4/8

# thus the final product is 1/4 * 2/5 * 1/5 * 1/2 = 1/100
# 100
