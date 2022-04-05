def combination(n, r):
    if n == r or r == 0:
        return 1
    return combination(n - 1, r - 1) + combination(n - 1, r)


n, r = list(map(int, input().split()))
print(combination(n, r))
