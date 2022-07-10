class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp=[0 for _ in range(len(cost)+1)]
        for i in range(2, len(dp)):
            dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
            
        return dp[-1]