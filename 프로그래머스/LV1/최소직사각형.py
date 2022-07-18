def solution(sizes):
    answer = 0
    maxW, maxH = 0,0
    for size in sizes:
        w, h = size
        if w < h:
            w, h= h, w
        maxW = w if maxW < w else maxW
        maxH = h if maxH < h else maxH
    
    return maxW*maxH