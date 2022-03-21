import math
def solution(str1, str2):
    answer=""
    str1, str2 = str1.upper(), str2.upper()
    
    temp1, temp2 = [], []
    for i in range(1, len(str1)):
        if not str1[i-1].isalpha() or not str1[i].isalpha():
            continue
        temp1.append(str1[i-1: i+1])
        
    for i in range(1, len(str2)):
        if not str2[i-1].isalpha() or not str2[i].isalpha():
            continue
        temp2.append(str2[i-1: i+1])
        
    intersection = []
    union = list(set(temp1+temp2))
    multiIntersectionLen, multiUnionLen = 0,0
    for u in union:
        compare1Count = [u==t for t in temp1].count(True)
        compare2Count = [u==t for t in temp2].count(True)
        multiIntersectionLen += min(compare1Count, compare2Count)
        multiUnionLen += max(compare1Count, compare2Count)
    
    answer = 65536 if multiUnionLen == 0 else math.floor(multiIntersectionLen / multiUnionLen * 65536)
    
    
    return answer