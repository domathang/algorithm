def solution(scores):
    answer = ''
    new_scores = [[] for _ in range(len(scores))]

    for i in range(len(scores)):
        for j in range(len(scores)):
            new_scores[i].append(scores[j][i])

    for i in range(len(new_scores)):
        a = new_scores[i].copy()
        max_score = max(new_scores[i])
        min_score = min(new_scores[i])
        avg = 0.0

        if max_score == new_scores[i][i]:
            a.remove(max_score)
            if max_score not in a:
                avg = sum(a) / len(a)
            else:
                avg = sum(new_scores[i]) / len(new_scores[i])
        elif min_score == new_scores[i][i]:
            a.remove(min_score)
            if min_score not in a:
                avg = sum(a) / len(a)
            else:
                avg = sum(new_scores[i]) / len(new_scores[i])
        else:
            avg = sum(new_scores[i]) / len(new_scores[i])

        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77],
                [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
                [24, 90, 94, 75, 65]]))
