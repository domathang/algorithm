k, n = map(int, input().split())
a = []
for i in range(k):
    a.append(int(input()))

s = 0
e = 2**32 - 1
m = e // 2
answer = 0

while True :
    cnt = 0
    for i in a:
        cnt += i // m
    if s == m or e == m:
        break
    elif cnt > n or cnt == n:
        s = m
    elif cnt < n:
        answer = k
        e = m
    m = (s + e) // 2
print(m)
