# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        cnt += 1
    if scoville[0] >= K:
        return cnt
    else:
        return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
