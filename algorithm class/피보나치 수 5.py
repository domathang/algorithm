def fibonaccci(n):
    if n < 2:
        return n
    return fibonaccci(n - 1) + fibonaccci(n - 2)


n = int(input())

print(fibonaccci(n))
