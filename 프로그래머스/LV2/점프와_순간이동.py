def solution(n):
    answer=0
    while n != 0:
        if n %2 == 1:
            answer+=1
        n = n//2
    return answer