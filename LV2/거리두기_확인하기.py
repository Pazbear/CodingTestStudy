def solution(places):
    answer = []
    
    direction=[[-1, 0],[0, 1], [1, 0], [0, -1]]
    
    
    for place in places:
        existPlace = []
        notRight=False
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    if not isRight(place, direction, i, j, i, j, 0):
                        notRight = True
                        break
            if notRight:
                break
        if notRight:
            answer.append(0)
        else:
            answer.append(1)
    return answer


def isRight(place, direction, curi, curj, i, j, level):
    if level == 0:
        for k in range(4):
            if i+direction[k][0]>=0 and i+direction[k][0]<5 and j+direction[k][1]>=0 and j+direction[k][1]<5:
                if place[i+direction[k][0]][j+direction[k][1]] == 'P':
                    return False
                elif place[i+direction[k][0]][j+direction[k][1]] == 'O':
                    if not isRight(place, direction,i,j, i+direction[k][0], j+direction[k][1], 1):
                            return False

    else:
        for k in range(4):
            if i+direction[k][0]>=0 and i+direction[k][0]<5 and j+direction[k][1]>=0 and j+direction[k][1]<5:
                if not (curi==i+direction[k][0] and curj==j+direction[k][1]):
                    if place[i+direction[k][0]][j+direction[k][1]] == 'P':
                        return False
    return True