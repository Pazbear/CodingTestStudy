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

#알파벳인가 아닌가
print('a'.isalpha())

#dict value로 정렬  내림차순
sorted(dict.items(), key=lambda a:a[1], reverse=True)

#배열 안에 중복된 값이 있는지 판단
if len(arr) == len(set(arr)):
    return True
else:
    return False