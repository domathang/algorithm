n, m = map(int, input().split())
books = list(map(int, input().split()))
negative = [abs(i) for i in books if i < 0]
positive = [i for i in books if i > 0]
negative.sort()
positive.sort()

answer = 0

start = len(positive) % m - 1
start = start if start != -1 else m-1
for i in range(start, len(positive) + m-1, m):
    answer += positive[i] * 2

start = len(negative) % m - 1
start = start if start != -1 else m-1
for i in range(start, len(negative) + m-1, m):
    answer += negative[i] * 2

print(answer - max(positive + negative))
