a, b = map(int, input().split())

def solution(a, b):
    months_sum = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    m = months_sum[a-1] + b
    m = (m-1) % 7
    answer = days[m]
    print(answer)
    return answer
