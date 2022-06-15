n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree - mid
    if cnt >= m:
        ans = mid
        start = mid + 1
    elif cnt < m:
        end = mid - 1

print(ans)
