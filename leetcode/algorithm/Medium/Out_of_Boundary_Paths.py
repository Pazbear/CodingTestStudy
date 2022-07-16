class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp=[[0 for _ in range(n)] for _ in range(m)]
        answer=0
        dp[startRow][startColumn]=1
        for _ in range(maxMove):
            temp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == m-1:
                        answer = (answer+dp[i][j])%1000000007
                    if j == n-1:
                        answer = (answer+dp[i][j])%1000000007
                    if i == 0:
                        answer = (answer+dp[i][j])%1000000007
                    if j == 0:
                        answer = (answer+dp[i][j])%1000000007
                    #사방의 DP배열로부터 값을 더해 올 수 있는 수를 구함
                    temp[i][j] = (((dp[i-1][j] if i > 0 else 0)+(dp[i+1][j] if i < m-1 else 0))% 1000000007 + ((dp[i][j-1] if j > 0 else 0)+(dp[i][j+1] if j < n-1 else 0))% 1000000007)%1000000007
            dp = temp
        return answer