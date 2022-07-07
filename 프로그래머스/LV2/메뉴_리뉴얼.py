import itertools
def solution(orders, course):
    answer = []
    available_course = {}
    for order in orders:
        order = ''.join(sorted(order))
        for i in course:
            if i > len(order):
                continue
            
            #가능한 콤비네이션을 모두 만든 후 그것이 중복될때마다 갯수 올림
            for c in list(map(''.join, itertools.combinations(order, i))):
                if c in available_course:
                    available_course[c]+=1
                else:
                    available_course[c]=1
                    
    #코스개수 별로 가장 많은 코스를 도출
    for c in course:
        maxn=0
        maxarr=[]
        for ac in available_course:
            if len(ac)==c:
                if available_course[ac]==1:
                    continue
                if maxn < available_course[ac]:
                    maxn=available_course[ac]
                    maxarr=[ac]
                elif maxn == available_course[ac]:
                    maxarr.append(ac)
        for ma in maxarr:
            answer.append(ma)
    return sorted(answer)