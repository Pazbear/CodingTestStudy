class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        curloc=[0, len(matrix[0])-1]
        while curloc[0]<=len(matrix)-1:
            x, y = curloc
            if matrix[x][y]==target:
                return True
            if matrix[x][y]>target:
                if y-1 <0:
                    curloc=[x+1, y]
                elif matrix[x][y-1]!=float(-inf):
                    curloc=[x, y-1]
                else:
                    curloc=[x+1, y]
            elif matrix[x][y]<target:
                if y+1>len(matrix[0])-1:
                    curloc=[x+1, y]
                elif matrix[x][y+1]!=float(-inf):
                    curloc=[x, y+1]
                else:
                    curloc=[x+1, y]
            matrix[x][y]=float(-inf)
        return False