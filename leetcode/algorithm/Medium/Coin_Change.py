class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[inf]*amount
        for x in range(1, amount+1):
            dp[x] = min(dp[x-c] if x-c >= 0 else inf for c in coins)+1
        return dp[amount] if dp[amount] != inf else -1
            