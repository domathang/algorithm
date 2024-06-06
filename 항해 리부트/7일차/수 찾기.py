n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arrm = list(map(int, input().split()))
arr.sort()
for i in arrm:
    s = 0
    m = n // 2
    e = n
    while s != m:
        if arr[m] == i:
            break
        elif arr[m] < i:
            s = m
        else:
            e = m
        m = (s + e) // 2

    if i == arr[m]:
        print(1)
    else:
        print(0)