def solution(n):
    answer = []
    hanoi(n, 1,3,2, answer)
    return answer

def hanoi(n, from_p, to_p, inter_p, answer):
    if n==1:
        answer.append([from_p, to_p])
        return
    hanoi(n-1, from_p, inter_p, to_p, answer)
    answer.append([from_p, to_p])
    hanoi(n-1, inter_p, to_p, from_p,answer)