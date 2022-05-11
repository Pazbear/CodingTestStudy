def solution(p):
    return fixP(p)

def fixP(p):
    if not p:
        return p
    if checkRight(p):
        return p
    left, right, index=0,0,0
    
    for i in p:
        if i == '(':
            left+=1
        else:
            right+=1
        index+=1
        if left == right:
            break
    
    u=p[:index]
    v=p[index:]
    ret=""
    if not checkRight(u):
        ret = "("+fixP(v)+")"+change(u[1:len(ret)-1])
        return ret
    else:
        return u+fixP(v)

def change(st):
    temp=""
    for i in range(len(st)):
        if st[i]=='(':
            temp+=')'
        else:
            temp+='('
    return temp
    
def checkRight(st):
    stack=[]
    for s in st:
        if s == '(':
            stack.append('s')
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True