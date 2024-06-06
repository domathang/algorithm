n, k = map(int, input().split())
info = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    info.append([a, b, c, d])
info.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(n):
    if info[i][0] == k:
        # 같은 등수가 아닐때까지
        j = i - 1
        while j >= 0 and info[j][1] == info[i][1] and info[j][2] == info[i][2] and info[j][3] == info[i][3]:
            j -= 1
        print(j + 2)
