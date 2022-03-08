n = int(input())

a = [int(input()) for _ in range(n)]

# 산술 평균
print(round(sum(a) / n))

# 중앙값
a.sort()
print(a[n//2])

# 최빈값
count = 1
max_count = 0
b = []
for i in range(1, n):
    if a[i-1] == a[i]:
        count += 1
    else:
        count = 1

    if max_count < count:
        max_count = count
        b = [a[i-1]]
    elif max_count == count:
        b.append(a[i-1])


if len(b) > 1:
    print(b[1])
elif len(a) == 1:
    print(a[0])
else:
    print(b[0])

# 범위
print(a[-1] - a[0])
