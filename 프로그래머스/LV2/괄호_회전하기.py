def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += isRight(s[i:]+s[0:i])
    return answer

def isRight(s):
    stack=[]
    for c in s:
        if c==']':
            if len(stack)==0:
                return 0
            temp = stack.pop()
            if temp !='[':
                return 0
        elif c==')':
            if len(stack)==0:
                return 0
            temp = stack.pop()
            if temp != '(':
                return 0
        elif c=='}':
            if len(stack)==0:
                return 0
            temp = stack.pop()
            if temp != '{':
                return 0
        else:
            stack.append(c)
    return 1 if len(stack) == 0 else 0