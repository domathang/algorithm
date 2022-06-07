n = int(input())
c = 0
for i in range(1, n+1):
    for j in str(i):
        if '3' == j or '6' == j or '9' == j:
            c += 1
print(c)
