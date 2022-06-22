from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer=0
        dic = defaultdict(int)
        dic[0]=1
        sumn=0 
        for num in nums:
            sumn += num
            answer+=dic[sumn-k] ## sumn-k ==> 현재까지의 배열에서 이전 서브배열을 뺀 값
            dic[sumn]+=1 ## 앞의 서브배열들의 집합 [1], [1,2], [1,2,3] ...
        return answer