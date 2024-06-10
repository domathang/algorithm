x, y = map(int, input().split())
z = y * 100 // x
if z == 100 or z == 99:
    print(-1)
else:
    l = 1
    r = x
    while l < r:
        m = (l+r)//2
        if (y+m) * 100 // (x+m) <= z:
            l = m + 1
        else:
            r = m
    print(r)
