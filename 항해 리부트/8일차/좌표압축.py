n = int(input())
lst = list(map(int, input().split()))
sl = sorted({*lst})
answer = {}
for i in range(len(sl)):
    answer[sl[i]] = i
print(*[answer[i] for i in lst])