import math
n = int(input())
friends = list(map(int, input().split()))
average = int(math.ceil(sum(friends)/n))
print(average)
x = 0
for i in friends:
    if average < i:
        x += i - average
print(x)
