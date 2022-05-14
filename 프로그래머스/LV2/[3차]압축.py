from string import ascii_uppercase
def solution(msg):
    answer = []
    dictionary = {}
    for i in range(len(ascii_uppercase)):
        dictionary[ascii_uppercase[i]]=i+1
    cur = msg[0]
    for m in msg[1:]:
        if cur+m not in dictionary:
            answer.append(dictionary[cur])
            dictionary[cur+m]=len(dictionary)+1
            cur=m
        else:
            cur+=m
    answer.append(dictionary[cur])
        
    return answer