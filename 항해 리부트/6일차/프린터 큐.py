n = int(input())
q = []
for i in range(n):
    a, b = map(int, input().split())
    idx = 0
    order = 0
    q = list(map(int, input().split()))
    while len(q) > 0:
        e = q.pop(0)
        if len(q) != 0 and max(q) > e:
            q.append(e)
            if idx == b:
                b += len(q)
        else:
            order += 1
            if idx == b:
                print(order)
                break   
        idx += 1
