from collections import defaultdict
def solution(a):
    answer = -1
    len_a = len(a)
    index_a = defaultdict(list)
    for i in range(len_a):
        index_a[a[i]].append(i)
    for arr in index_a:
        i = 0
        last_used = -1
        len_star = 0
        for i in index_a[arr]:
            if (i== len_a-1 and last_used>=i-1):
                continue
            elif i==0 or last_used >= i-1:
                if a[i]==a[i+1]:
                    last_used = i+1
                    continue
                last_used = i+1
            else:
                if a[i]==a[i-1]:
                    last_used = i
                    continue
                last_used = i
            len_star+=2
        answer = max(len_star, answer)
    return answer