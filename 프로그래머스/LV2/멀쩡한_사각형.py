def solution(w,h):
    if w >= h:
        return w*h -(w+h) + gcd(w, h)
    else:
        return w*h -(w+h) + gcd(h, w)

#최대공약수
def gcd(a, b):
    if b==0: return a
    return gcd(b, a%b)