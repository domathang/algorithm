n = int(input())
k = int(input())
sensor = list(set(map(int, input().split())))
sensor.sort()
diff = []
for i in range(1, len(sensor)):
    diff.append(sensor[i] - sensor[i-1])
diff.sort(reverse=True)
print(sum(diff[k-1:]))
