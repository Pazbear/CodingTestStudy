def solution(n, t, m, p):
    answer=""
    str = "0"
    i=1
    cnt=0
    while cnt < t:
        str+=convert(n, i)
        i+=1
        while len(str)>m*cnt+(p-1):
            answer+=str[m*cnt+(p-1)]
            cnt+=1
            if cnt>=t:
                break
    return answer

def convert(n, num):
    res = []
    while num > 0:
        num, mod = divmod(num, n)
        mod = 'A' if mod == 10 else 'B' if mod ==11 else 'C' if mod==12 else 'D' if mod==13 else 'E' if mod==14 else 'F' if mod == 15 else mod
        res.append(str(mod))
    return ''.join(res[::-1]) ## 리스트 역순