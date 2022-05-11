"""
110을 모두 뽑아 수를 센 후 0이 들어왔을 때 110을 전부 추가하고 나머지 추가
"""
from collections import deque
def solution(s):
    answer = []
    for number in s:
        stack=[]
        count =0
        for nch in number:
            if nch=='0':
                if stack[-2:]==['1','1']:
                    count+=1
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(nch)
            else:
                stack.append(nch)
        fixednumber = deque()
        while stack:
            if stack[-1] == '1':
                fixednumber.append(stack.pop())
            else:
                break
        while count >0:
            fixednumber.appendleft('0')
            fixednumber.appendleft('1')
            fixednumber.appendleft('1')
            count-=1
        while stack:
            fixednumber.appendleft(stack.pop())
        answer.append(''.join(fixednumber))
    return answer