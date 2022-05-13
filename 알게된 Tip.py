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
    res= True
else:
    res= False

#2차원 배열 90도 돌리기
for i in range(n):
    for j in range(m):
        result[j][n-i-1] = a[i][j]

#x의 제곱
print(x ** 3) # x의 3제곱

#2진수 변환
print(bin(301))

#두 직선의 교점
print("Ax + By + E = 0")
print("Cx + Dy + F = 0")
print("두 직선의 교점은 ")
print("x = (B*F - E*D) / (A*D - B*C) ")
print("y = (E*C - A*F) / (A*D - B*C) ")

#얇은 복사, 깊은 복사
import copy
a=1
b=a
if a is b:
    print("true - 얇은 복사(메모리 주소가 같음)")
b = copy.deepcopy(a)
if a is b:
    print("false - 깊은 복사(메모리 주소 다름)")

#값이 비정상적으로 커 효율성을 중시하는 문제처럼 보일 경우
#이분탐색을 고려해봐야함


#문자열에서 특정 규칙의 문자열을 뽑아내야할 때
import re
#를 고려해봐야함


#bfs,dfs 시 board 의 예외처리 편의를 위해
#일부러 상하좌우에 한줄의 board를 더 추가함으로써 좌표가 -1이 되었을때의 indexerr를 무시함.


#가장 큰 정사각형 찾기 (dp)
board[i][j] = min(board[i-1][j-1], min(board[i][j-1],board[i-1][j]))+1
#으로 dp 배열을 만든 후 가장 큰 수를 제곱