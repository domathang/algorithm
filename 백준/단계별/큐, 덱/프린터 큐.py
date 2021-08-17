t = int(input())
importance = []
for _ in range(t):
    n, m = map(int, input().split())
    importance = [int(x) for x in input().split()]
    cnt = 0
    while importance:
        if max(importance) == importance[0]:
            importance.pop(0)
            cnt += 1
            if m == 0:
                break
            else:
                m -= 1
        else:
            importance.append(importance.pop(0))
            if m == 0:
                m = len(importance) - 1
            else:
                m -= 1
    print(cnt)
