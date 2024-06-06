import math
n = int(input())

for i in range(n):
    m = int(input())
    kinds = {}
    for j in range(m):
        clothes, kind = input().split()
        if kind in kinds:
            kinds[kind] += 1
        else:
            kinds[kind] = 1
    ans = 1
    for j in kinds:
        ans *= (kinds[j]+1)
    print(ans-1)