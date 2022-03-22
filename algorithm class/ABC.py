arr = list(map(int, input().split()))
ABC = input()

# 선택 정렬
for i in range(3):
    index = arr.index(min([arr[i] for i in range(i, 3)]))
    arr[i], arr[index] = arr[index], arr[i]

d = {"A": arr[0], "B": arr[1], "C":arr[2]}

for i in ABC:
    print(d[i], end=" ")
