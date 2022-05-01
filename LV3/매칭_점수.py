import re
def solution(word, pages):
    answer = 0
    urls = []
    ex_urls= []
    score = []
    link = dict()
    for page in pages:
        tu = re.search(r'(<meta property.+content=")(https://.*)"/>', page).group(2)
        urls.append(tu) #현재 url검색
        link[tu]=0
        ex_urls.append(list(map(extractURL, re.findall(r'<a href="https://\S*">', page)))) #외부 링크 url 전부 검색     
        s = 0
        word = word.lower()
        page = page.lower()
        for w in re.findall('[a-z]+', page): #페이지 전체에서 단어검색
            if w == word:
                s += 1
        score.append(s)
    for i in range(len(ex_urls)):
        for j in range(len(ex_urls[i])):
            if ex_urls[i][j] in link:
                link[ex_urls[i][j]]+=score[i] / len(ex_urls[i])
    maxnum = 0
    for i in range(len(score)):
        if maxnum < score[i]+link[urls[i]]:
            maxnum = score[i]+link[urls[i]]
            answer = i
    return answer
    
def extractURL(s):
    return s[9:-2]