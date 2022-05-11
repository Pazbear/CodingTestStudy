def solution(arr):
    return dfs(arr, 0, 0, len(arr))

def dfs(arr, x, y, n):
    if n == 1:
        return [1, 0] if arr[x][y] == 0 else [0, 1]
    sum1 = 0
    lensum = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            sum1+=arr[i][j]
    if sum1 == n*n or sum1 == 0:
        return [0, 1] if sum1 >0 else [1,0]
    else:
        cntxy = [0,0]
        #1사분면
        firstxy = dfs(arr, x, y, n//2)
        #2사분면
        secondxy = dfs(arr, x+n//2, y, n//2)
        #3사분면
        thirdxy = dfs(arr, x, y+n//2, n//2)
        #4사분면
        fourthxy = dfs(arr, x+n//2, y+n//2, n//2)
        cntxy[0] = firstxy[0]+secondxy[0]+thirdxy[0]+fourthxy[0]
        cntxy[1] = firstxy[1]+secondxy[1]+thirdxy[1]+fourthxy[1]
        return cntxy