n = int(input())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
lst.sort()
stac = []
answer = 0
for i in lst:
    height = i[1]
    while stac and stac[-1] > height:
        stac.pop()
        answer += 1
    if height and (len(stac) == 0 or stac[-1] != height):
        stac.append(height)
print(answer + len(stac))
    