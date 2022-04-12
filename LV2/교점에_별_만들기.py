def solution(line):
    answer = []
    points = []
    minX, minY, maxX, maxY = 1000000000000000,1000000000000000, -1000000000000000,-1000000000000000
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            point = getCrossPoint(line[i], line[j])
            if point == -1:
                continue
            minX = min(minX, int(point[0]))
            minY = min(minY, int(point[1]))
            maxX = max(maxX, int(point[0]))
            maxY = max(maxY, int(point[1]))
            points.append([int(point[0]), int(point[1])])
    board = [['.' for _ in range(minX, maxX+1)] for _ in range(minY, maxY+1)]
    lenX, lenY = maxX-minX, maxY-minY
    for p in points:
        board[maxY-p[1]][p[0]-minX]='*'
    return [''.join(b) for b in board]

def getCrossPoint(l1, l2):
    a, b, e = l1
    c, d, f = l2
    
    if a*d-b*c ==0:
        return -1
    
    x = (b*f - e*d)/(a*d-b*c)
    y = (e*c - a*f)/(a*d-b*c)
    if x == int(x) and y == int(y):
        return [x, y]
    else:
        return -1