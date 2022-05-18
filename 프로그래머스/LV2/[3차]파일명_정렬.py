def solution(files):
    answer = []
    arr = []
    for fileindex in range(len(files)):
        isNum = False
        head, number = "",""
        file = files[fileindex]
        #헤드, 넘버 나누기
        for i in range(len(file)):
            if isNum:
                if not file[i].isdigit():
                    break
                else:
                    number+=file[i]
            elif file[i].isdigit():
                number+=file[i]
                isNum=True
            if not isNum:
                head+=file[i]
        arr.append([fileindex,head.upper(), int(number)])
    #정렬된 인덱스로 정답 찾기
    for a in sorted(arr, key=lambda x : (x[1],x[2])):
        answer.append(files[a[0]])
    return answer