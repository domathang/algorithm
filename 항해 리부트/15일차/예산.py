n = int(input())
req = list(map(int,input().split()))
m = int(input())


l = 1
r = max(req)
while l <= r:
    mid = (l+r) // 2
    tot = sum([mid if i > mid else i for i in req])
    if tot <= m:
        l = mid + 1
    elif tot > m:
        r = mid - 1
print(r)