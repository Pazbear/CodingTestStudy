import math

def solution(left, right):
    answer=0
    for num in range(left, right+1):
        if isSqrt(num):
            answer-=num
        else:
            answer+=num
    return answer

def isSqrt(num):
    sqrt=math.sqrt(num)
    if sqrt == int(sqrt):
        return True
    else:
        return False