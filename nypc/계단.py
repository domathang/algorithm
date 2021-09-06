m, f, n = map(int, input().split())
cnt = 0
if m != f:
    cnt = 1
    n -= m - f
cnt += n // (m-1)
if n % (m-1) != 0 and n % (m-1) >= f:
    cnt += 1
print(cnt)
