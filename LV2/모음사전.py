def solution(word):
    answer=0
    numOfWords = 5
    maxn = 0
    for i in range(1, numOfWords+1):
        maxn+=pow(numOfWords, i)
    for i in range(1, len(word)+1):
        if word[i-1] == 'A':
            answer+=1
        elif word[i-1]=='E':
            answer+= ((maxn//pow(numOfWords, i))*1)+1
        elif word[i-1]=='I':
            answer+= ((maxn//pow(numOfWords, i))*2)+1
        elif word[i-1]=='O':
            answer+= ((maxn//pow(numOfWords, i))*3)+1
        else:
            answer+= ((maxn//pow(numOfWords, i))*4)+1
    return answer