#dictionary에 값이 있는지 확인할 때

if item in dictionay:
    print("있음")
else:
    print("없음")

#최대공약수
def gcd(a, b):
    if b==0: return a
    return gcd(b, a%b)

#문자열 거꾸로
''.join(reversed(list(str)))