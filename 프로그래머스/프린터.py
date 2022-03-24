def solution(priorities, location):
    answer = 0
    while True:
        p = priorities.pop(0)
        if not priorities or p >= max(priorities):
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1
        else:
            priorities.append(p)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))