n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
q = [0] * w

time = 0
while trucks or sum(q) > 0:
    q.pop(0)
    if trucks and sum(q) + trucks[0] <= l:
        truck = trucks.pop(0)
        q.append(truck)
    else:
        q.append(0)
    time += 1
print(time)