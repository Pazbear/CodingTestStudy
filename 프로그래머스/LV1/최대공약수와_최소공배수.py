def solution(n, m):
    answer = []
    answer.append(gcd(n, m) if n>m else gcd(m, n))
    answer.append(lcm(n, m) if n>m else lcm(m, n))
    return answer

def lcm(n, m):
    cnt=1
    while True:
        if cnt*n %m ==0:
            return cnt*n
        cnt+=1
    return cnt*n
    
def gcd(n, m):
    if m==0:
        return n
    return gcd(m, n%m)