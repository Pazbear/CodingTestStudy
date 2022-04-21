"""
del - 와 pop()의 차이점
del은 pop()과 달리 값을 반환하지 않음
하지만 속도가 더 빠름
"""
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    cache = deque()
    for city in cities:
        if city.upper() in cache:
            answer +=1
            del cache[cache.index(city.upper())]
        else:
            answer +=5
            if len(cache)>=cacheSize:
                cache.popleft()
        cache.append(city.upper())
    return answer