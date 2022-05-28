def solution(arr):
    len_arr = len(arr)
    LCM=0
    if len_arr ==1:
        return arr[0]
    elif len_arr ==2:
        return findLCM(arr[0],arr[1])
    else:
        LCM = findLCM(arr[0],arr[1])
        for i in range(2, len_arr):
            LCM = findLCM(LCM, arr[i])
    return LCM

def findLCM(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    i=1
    while (num2*i)%num1 !=0:
        i+=1
    return num2*i