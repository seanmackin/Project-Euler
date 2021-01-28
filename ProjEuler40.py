txt = ""

for i in range(1,1000001):
    txt = txt + str(i)

ans = int(txt[0]) * int(txt[10-1]) * int(txt[100-1]) * int(txt[1000-1]) * int(txt[10000-1]) * int(txt[100000-1]) * int(txt[1000000-1])

print(ans)

#ans: 210
