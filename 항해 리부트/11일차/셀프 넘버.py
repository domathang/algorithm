check =  [0] * 10001
for i in range(1, 10001):
    tot = i
    k = i
    while k :
        tot += k % 10
        k //= 10
    if tot < 10001:
        check[tot] = 1
for i in range(1, 10001):
    if check[i] == 0:
        print(i)

