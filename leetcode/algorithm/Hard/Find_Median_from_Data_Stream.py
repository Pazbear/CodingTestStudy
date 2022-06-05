import heapq
class MedianFinder:
    def __init__(self):
        self.len_arr = 0
        self.low_heap = []
        self.high_heap = []

    def addNum(self, num: int) -> None:
        if not self.low_heap or num < -self.low_heap[0]:
            heapq.heappush(self.low_heap, -num)
        else:
            heapq.heappush(self.high_heap, num)
        
        if abs(len(self.low_heap) - len(self.high_heap))>=2:
            if len(self.low_heap) > len(self.high_heap):
                heapq.heappush(self.high_heap, -heapq.heappop(self.low_heap))
            else:
                heapq.heappush(self.low_heap, -heapq.heappop(self.high_heap))
        self.len_arr+=1
    def findMedian(self) -> float:
        if self.len_arr%2 ==0:
            return (self.high_heap[0]-self.low_heap[0])/2
        else:
            if len(self.low_heap) > len(self.high_heap):
                return -self.low_heap[0]
            else:
                return self.high_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()