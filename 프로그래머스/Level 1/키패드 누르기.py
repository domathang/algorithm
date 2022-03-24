def solution(numbers, hand):
    answer = ''
    pad = [[1, 4, 7, -1],
           [2, 5, 8, 0],
           [3, 6, 9, -1]]
    cur_l = cur_r = -1
    left_line = 0
    right_line = 2
    for n in numbers:
        if n in pad[2]:
            cur_r = n
            answer += 'R'
            right_line = 2
        elif n in pad[0]:
            cur_l = n
            answer += 'L'
            left_line = 0
        else:
            if abs(1 - right_line) + abs(pad[1].index(n) - pad[right_line].index(cur_r))\
                    > abs(1 - left_line) + abs(pad[1].index(n) - pad[left_line].index(cur_l)):
                cur_l = n
                left_line = 1
                answer += 'L'
            elif abs(1 - right_line) + abs(pad[1].index(n) - pad[right_line].index(cur_r))\
                    < abs(1 - left_line) + abs(pad[1].index(n) - pad[left_line].index(cur_l)):
                cur_r = n
                right_line = 1
                answer += 'R'
            else:
                if hand == 'right':
                    answer += 'R'
                    cur_r = n
                    right_line = 1
                else:
                    answer += 'L'
                    cur_l = n
                    left_line = 1
    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
