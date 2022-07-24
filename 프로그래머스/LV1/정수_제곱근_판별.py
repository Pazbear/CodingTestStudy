import math
def solution(n):
    temp = math.sqrt(n)
    return (temp+1)**2 if temp == int(temp) else -1