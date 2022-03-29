n = int(input())
a = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

a.sort()

for i in ms:
    l = 0
    r = n - 1
    mid = (l + r) // 2
    x = 0
    while l <= r:
        if a[mid] > i:
            r = mid - 1
        elif a[mid] < i:
            l = mid + 1
        else:
            x = 1
            break
        mid = (l + r) // 2
    print(x)
