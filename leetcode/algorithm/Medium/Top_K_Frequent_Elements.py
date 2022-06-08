from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num]+=1
        answer = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        return [answer[i][0] for i in range(k)]