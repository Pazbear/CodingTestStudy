class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        answer=[[0 for _ in range(i+1)] for i in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if j==0 or j ==i:
                    answer[i][j]=1
                else:
                    answer[i][j]=answer[i-1][j-1]+answer[i-1][j]
        return answer