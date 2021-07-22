n = int(input())
time = list(map(int, input().split(' ')))
time.sort()
sum = 0
before_sum = 0
for t in time:
    sum += before_sum + t
    before_sum += t
print(sum)
