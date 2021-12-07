import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        s1 = heapq.heappop(scoville)

        if s1 >= K:
            return answer

        if len(scoville) == 0:
            return -1

        s2 = heapq.heappop(scoville)

        heapq.heappush(scoville, s1 + (s2 * 2))
        answer += 1


print(solution([1, 2, 3, 9, 10, 12], 7))
