def solution(x):
    return True if x % sum(list(map(int, list(str(x))))) ==0 else False