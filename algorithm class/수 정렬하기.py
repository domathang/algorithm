n = int(input())

arr = [int(input()) for _ in range(n)]

# 삽입 정렬
for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(i)
