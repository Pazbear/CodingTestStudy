def solution(s):
    cnt=0
    zerocnt=0
    
    while s != '1':
        onecnt = s.count('1')
        zerocnt += len(s)-onecnt
        cnt+=1
        s=str(bin(onecnt))[2:]
    
    return [cnt, zerocnt]