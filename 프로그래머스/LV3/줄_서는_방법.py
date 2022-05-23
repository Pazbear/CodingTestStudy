import math
def solution(n, k):
    result=[]
    arr=[i for i in range(1, n+1)]
    for i in range(n-1, 0, -1):
        temp = max(math.factorial(i),2)
        result.append(arr[(k-1)//temp])
        del arr[(k-1)//temp]
        k=k%temp
    result.append(arr[0])
    return result