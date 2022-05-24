import heapq
import math
def solution(n, works):
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap,-work)
    for i in range(n):
        temp=heapq.heappop(heap)
        heapq.heappush(heap,temp+1 if temp<0 else 0)
    while heap:
        answer+=math.pow(heapq.heappop(heap),2)
    return int(answer)