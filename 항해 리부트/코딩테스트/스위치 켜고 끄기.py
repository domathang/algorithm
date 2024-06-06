n = int(input())
switches = list(map(int, input().split()))
student = int(input())
students = [list(map(int, input().split())) for _ in range(student)]
for g, num in students:
    if g == 1:
        for i in range(num, n + 1, num):
            if switches[i - 1] == 0:
                switches[i - 1] = 1
            else:
                switches[i - 1] = 0
    else:
        i = 0
        # print(switches[num - (i + 1) - 1 : num - 1][::-1], switches[num : num + (i + 2) - 1])
        while num - (i + 1) - 1 > -1 and num + (i + 2) - 1 <= n and switches[num - (i + 1) - 1 : num - 1][::-1] == switches[num : num + (i + 2) - 1]:
            i += 1
        # print(i)
        for j in range(num - i-1, num+i):
            if switches[j] == 0:
                switches[j] = 1
            else:
                switches[j] = 0
    # print(switches)
for i in range(0, n, 20):
    print(*switches[i:i+20])
