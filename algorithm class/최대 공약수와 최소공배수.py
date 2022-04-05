def gcd(n, m):
    if n % m == 0:
        return m
    if n % m > 0:
        return gcd(m, n % m)


a, b = list(map(int, input().split()))
g = gcd(a, b)
print(g)
print(a * b // gcd(a, b))
