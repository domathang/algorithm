import sys

input = sys.stdin.readline

def key(i, j):
    return f"{i},{j}"

def bfs(max_weight):
    q = [f1]
    check = [0] * (n+1)
    check[f1] = 1
    while q:
        p = q.pop(0)
        if p == f2:
            return True
        for i in lst[p]:
            if check[i] == 0 and max_weight <= weight[key(p, i)]:
                q.append(i)
                check[i] = 1
    return False

if __name__ == '__main__':

    n, m = map(int, input().split())
    lst = [[] for _ in range(n + 1)]
    weight = {}

    for i in range(m):
        a, b, c = map(int, input().split())

        bridge = key(a, b)
        
        if bridge not in weight:
            lst[a].append(b)
            lst[b].append(a)
            weight[bridge] = weight[key(b, a)] = c

        if weight[bridge] < c:
            weight[bridge] = weight[key(b, a)] = c

    f1, f2 = map(int, input().split())
    
    l = min(weight.values())
    r = max(weight.values())
    answer = 1
    while l <= r:
        mid = (l+r) // 2
        if bfs(mid):
            l = mid + 1
            answer = mid
        else:
            r = mid - 1

    print(answer)
