n = int(input())
for i in range(n):
    m = int(input())
    l = 1
    r = m
    while l <= r:
        mid = (l + r) // 2
        if (mid * (mid + 1)) // 2 <= m:
            l = mid + 1
        else:
            r = mid - 1
    print(l-1)
