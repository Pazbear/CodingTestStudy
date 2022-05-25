def solution(A,B):
    answer = 0

    A.sort(reverse=True)
    B.sort()
    while A:
        answer += A.pop()*B.pop()

    return answer