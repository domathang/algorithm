n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 0
next_meet_start = 0
for start, end in meetings:
    if next_meet_start <= start:
        cnt += 1
        next_meet_start = end
print(cnt)