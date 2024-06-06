k = int(input())
side = []
max_width = 0
max_height = 0

for i in range(6):
    a, b = map(int, input().split())
    if a == 1 or a == 2:
        max_width = max(max_width, b)
    else:
        max_height = max(max_height, b)
    side.append((a, b))

small_rectangle = []

for i in range(6):
    # 같은 방향 변 사이에 입력된 변이라면
    if side[i-1][0] == side[(i+1) % 6][0]:
        small_rectangle.append(side[i][1])

print((max_width * max_height - small_rectangle[0] * small_rectangle[1]) * k)