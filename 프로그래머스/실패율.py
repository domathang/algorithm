def solution(N, stages):
    passed = [0] * (N+2)
    failure = []

    for i in stages:
        for j in range(i+1):
            passed[j] += 1

    for i in range(1, N+1):
        if passed[i] == 0:
            failure.append([0.0, i])
        else:
            failure.append([stages.count(i)/passed[i], i])

    failure.sort(key=lambda x : (x[0], N-x[1]), reverse=True)

    answer = [i[1] for i in failure]

    return answer

print(solution(4, [4,4,4,4,4]))