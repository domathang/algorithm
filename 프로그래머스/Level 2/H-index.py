# 내 풀이
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        while citations[i] >= answer + 1 and len(citations) - i >= answer + 1:
            answer += 1
    return answer





# 다른 사람의 풀이. 너무 깔끔해서 가져옴.
# 해설: https://hwan-hobby.tistory.com/260
def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
