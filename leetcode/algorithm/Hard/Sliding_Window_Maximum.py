from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        answer=[]
        for i in range(len(nums)):
            while queue and queue[-1][0]<=nums[i]:
                queue.pop()
            queue.append((nums[i], i))
            if i-queue[0][1]>=k:
                queue.popleft()
            if i>=k-1:
                answer.append(queue[0][0])
        return answer