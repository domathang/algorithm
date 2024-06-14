n = int(input())
expected_rank = [int(input()) for _ in range(n)]
expected_rank.sort()
k = 1
bad = 0
for i in range(1, n+1):
    bad += abs(expected_rank[i-1] - k)
    k += 1
print(bad)