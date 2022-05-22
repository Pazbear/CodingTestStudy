def solution(n):
    answer = 0
    cnt1 = countBin1(n)
    while True:
        n+=1
        if countBin1(n) == cnt1:
            return n

def countBin1(num):
    return bin(num)[2:].count('1')