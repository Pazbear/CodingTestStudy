class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if int(matrix[i][j])==1:
                    matrix[i][j]=min(int(matrix[i-1][j-1]), min(int(matrix[i-1][j]), int(matrix[i][j-1])))+1
        return max([max(list(map(int, matrix[i]))) for i in range(len(matrix))])**2