x, y = map(int, input().split())

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
cnt = [31, 28, 31, 30, 31, 30 ,31, 31 ,30 ,31 ,30 ,31]

# 시작 요일이 월요일일 때
start = 1

# 다음달 시작 요일 계산
for i in range(x-1):
    start = (start + (cnt[i] % 7)) % 7

print(week[(start + (y % 7) - 1) % 7])