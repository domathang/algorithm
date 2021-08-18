def solution(n, lost, reserve):
    s1 = set(lost)
    s2 = set(reserve)
    lost1 = list(s1 - s2)
    reserve1 = list(s2 - s1)
    answer = n-len(lost1)
    for i in range(len(lost1)):
        for j in range(len(reserve1)):
            if lost1[i] == reserve1[j]-1 :
                reserve1[j] = -100
                lost1[i] = 0
                answer += 1
            elif lost1[i] == reserve1[j]+1 :
                reserve1[j] = -100
                lost1[i] = 0
                answer += 1
    return answer