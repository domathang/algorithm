n, s = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0

def dfs(i, tot):
    global answer
    if tot == s:
        answer += 1
    for j in range(i+1, n):
        dfs(j, tot + lst[j])
    
for i in range(n):
    dfs(i, lst[i])
print(answer)
