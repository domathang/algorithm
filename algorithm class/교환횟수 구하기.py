n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp
            cnt += 1

print(arr)
print(cnt)
