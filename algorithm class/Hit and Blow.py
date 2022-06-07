n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c1 = 0
c2 = 0

for i in range(n):
    if a[i] == b[i]:
        c1 += 1
    if a[i] in b:
        c2 += 1

print(c1)
print(c2-c1)
