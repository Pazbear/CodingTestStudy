def solution(s):
    answer = []
    s= [a.split(',') for a in s[2:-2].split("},{")]
    cnt = dict()
    for a in s:
        for el in a:
            if int(el) in cnt:
                cnt[int(el)]+=1
            else:
                cnt[int(el)]=0
    return list(dict(sorted(cnt.items(), key=lambda a:a[1], reverse=True)).keys())