def solution(arr):
    prev_value=-1
    answer=[]
    for num in arr:
        if num == prev_value:
            continue
        answer.append(num)
        prev_value=num
    return answer