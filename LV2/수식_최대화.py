from itertools import permutations
def solution(expression):
    answer=0
    number=""
    arr=[]
    operator = ['-', '+', '*']
    
    for e in expression:
        if e in operator:
            arr.append(int(number))
            number=""
            arr.append(e)
        else:
            number += e
    if number:
        arr.append(int(number))
    for op in list(permutations(operator)):
        answer = max(answer, abs(calculate(arr, op)))
    
    return answer

def calculate(arr, op):
    for o in op:
        stack=[]
        i=0
        while i<len(arr):

            if arr[i] == o:
                if arr[i]=='*':
                    stack.append(stack.pop()*arr[i+1])
                elif arr[i]=='+':
                    stack.append(stack.pop()+arr[i+1])
                else:
                    stack.append(stack.pop()-arr[i+1])
                i+=1
            else:
                stack.append(arr[i])
            i+=1
        arr = stack
    return arr[0]