n, k = map(int, input().split())
arr = []
josephus = []
for i in range(n):
    arr.append(i + 1)
cnt = 0
for i in range(1, k*n+1):
    tmp = arr.pop(cnt)
    if i % k == 0:
        josephus.append(tmp)
    else:
        arr.append(tmp)
print("<", end="")
for i in range(len(josephus)):
    print(josephus[i], end="")
    if i == len(josephus)-1:
        print(">")
    else:
        print(", ", end="")
