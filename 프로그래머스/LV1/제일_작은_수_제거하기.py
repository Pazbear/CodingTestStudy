def solution(arr):
    minn=min(arr)
    arr=list(filter(lambda x: x!=minn, arr))
    return arr if arr else [-1]