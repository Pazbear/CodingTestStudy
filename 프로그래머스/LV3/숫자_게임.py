import heapq
def solution(A, B):
    answer = 0
    a = [-i for i in A]
    b = [-i for i in B]
    heapq.heapify(a)
    heapq.heapify(b)
    while a and b:
        ta = heapq.heappop(a)
        tb = heapq.heappop(b)
        if -ta < -tb:
            answer+=1
        else:
            heapq.heappush(b, tb)
        
        
    return answer