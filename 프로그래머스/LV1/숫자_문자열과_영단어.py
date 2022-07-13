words = dict()
def solution(s):
    answer = ""
    init()
    start= -1
    for i in range(len(s)):
        if s[i].isalpha():
            if start==-1:
                start=i
            elif s[start:i+1] in words:
                answer+= words[s[start:i+1]]
                start=-1
        else:
            answer+=s[i]
        
            
    return int(answer)
def init():
    words["zero"]='0'
    words["one"]='1'
    words["two"]='2'
    words["three"]='3'
    words["four"]='4'
    words["five"]='5'
    words["six"]='6'
    words["seven"]='7'
    words["eight"]='8'
    words["nine"]='9'