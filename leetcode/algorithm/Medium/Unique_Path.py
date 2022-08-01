class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = [[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j ==0:
                    answer[i][j] = 1
                else:
                    answer[i][j]=answer[i-1][j]+answer[i][j-1]
        return answer[m-1][n-1]