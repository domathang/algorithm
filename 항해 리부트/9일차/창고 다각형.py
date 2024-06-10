n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort()

area = 0
left_before = lst[0]
right_before = lst[-1]

for i in range(1, n):

    if lst[i][1] > left_before[1]:
        area += (lst[i][0] - left_before[0]) * left_before[1]
        left_before = lst[i]

    k = n - 1 - i
    if lst[k][1] > right_before[1]:
        area += (right_before[0] - lst[k][0]) * right_before[1]
        right_before = lst[k]

area += (right_before[0] - left_before[0] + 1) * left_before[1]

print(area)
