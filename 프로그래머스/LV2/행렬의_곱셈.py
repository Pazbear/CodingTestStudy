def solution(arr1, arr2):
    answer=[[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for arr1_i in range(len(arr1[0])):
                answer[i][j] += arr1[i][arr1_i]*arr2[arr1_i][j]
    return answer