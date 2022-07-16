def solution(d, budget):
    answer=0
    d.sort()
    for c in d:
        if budget< c:
            break
        else:
            budget-=c
            answer+=1

    return answer