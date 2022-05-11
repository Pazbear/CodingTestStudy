"""
정답 참고
"""
def solution(a):
    def input_min(k):
        q = []
        t = k[0]
        for x in k:
            if t > x:
                t = x # [0:0] ~ [0:n]까지 최소값을 도출
            q.append(t)
        return q
    #인덱스 기준으로 왼쪽의 최솟값이나 오른쪽의 최솟값보다 작으면 되므로
    #왼쪽을 돌며 최솟값을 구한 리스트와 오른쪽을 돌며 최솟값을 구한 리스트를 set 하면
    #왼쪽이나 오른쪽 둘중 하나는 최솟값인 값들의 리스트가 나옴
    return len(set(input_min(a) + input_min(list(reversed(a)))))