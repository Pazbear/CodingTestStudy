class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        
        dp = {0}
        for num in nums:
            next_dp = dp.copy()
            for t in dp:
                if t == target:
                    return True
                next_dp.add(t + num)
            dp = next_dp
        return False