def solution(n, arr1, arr2):
    answer = [[' ' for _ in range(n)] for _ in range(n)]
    for i,two_nums in enumerate(zip(arr1, arr2)):
        num1, num2 = two_nums
        bin_num1 = bin(num1)[2:]
        bin_num2 = bin(num2)[2:]
        num1_s = n-len(bin_num1)
        num2_s = n-len(bin_num2)
        for j in range(num1_s, n):
            answer[i][j] = '#' if bin_num1[j-num1_s] == '1' else ' '
        for j in range(num2_s,n):
            if answer[i][j] == ' ':
                answer[i][j] = '#' if bin_num2[j-num2_s] == '1' else ' '
    for i in range(len(answer)):
        answer[i]=''.join(answer[i])
    return answer