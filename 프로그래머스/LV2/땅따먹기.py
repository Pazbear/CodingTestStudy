def solution(land):
    for i in range(len(land)-1):
        arr = [(land[i][j], j) for j in range(len(land[i]))]
        arr = sorted(arr, key = lambda key:key[0], reverse=True)
        for j in range(len(land[i])):
            if j == arr[0][1]:
                land[i+1][j]+=arr[1][0]
            else:
                land[i+1][j]+=arr[0][0]
    return max(land[-1])