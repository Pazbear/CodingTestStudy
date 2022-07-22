def solution(s):
    word_index=0
    answer=''
    for i in range(len(s)):
        if s[i]==' ':
            word_index=0
            answer+=s[i]
        else:
            answer+=s[i].upper() if word_index%2==0 else s[i].lower()
            word_index+=1
    return answer