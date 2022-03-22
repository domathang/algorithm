arr = list(map(int, input().split()))

# 버블
for i in range(3):
    for j in range(3-i-1):
        if arr[j] > arr[j+1]:
            arr[j+1], arr[j] = arr[j], arr[j+1]

for i in arr:
    print(i, end=" ")
