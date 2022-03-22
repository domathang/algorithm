n, m = list(map(int, input().split()))

arr = list(range(1, n+1))

for i in range(m):
    swap_n, swap_m = list(map(int, input().split()))
    arr[swap_n-1], arr[swap_m-1] = arr[swap_m-1], arr[swap_n-1]

for i in arr:
    print(i, end=" ")
