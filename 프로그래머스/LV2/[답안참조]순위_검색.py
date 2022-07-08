#답안참조
from collections import defaultdict
import itertools
import bisect
def solution(info, query):
    infomap = defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    #모든 경우의 가능한 쿼리를 dict에 point와 함께 넣음
    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)]) 
            infomap[key].append(int(inf[4]))

    for k in infomap.keys():
        infomap[k].sort()
    
    answers = []
    for q in query:
        l,_,p,_,c,_,f, point = q.split()
        key = ''.join([l,p,c,f])
        #알맞은 list에서 point이상의 개수를 이분탐색으로 검색
        i = bisect.bisect_left(infomap[key], int(point))
        answers.append(len(infomap[key]) - i)

    return answers