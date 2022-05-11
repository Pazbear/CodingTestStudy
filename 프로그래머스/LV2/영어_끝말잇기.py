def solution(n, words):
    answer = [0,0]
    prev=""
    mem = set()
    for i in range(len(words)):
        if words[i] in mem:
            return [i%n+1, i//n+1]
        if prev != "":
            if words[i][0] == prev:
                prev = words[i][-1]
            else:
                return [i%n+1, i//n+1]
        else:
            prev = words[i][-1]
        mem.add(words[i])
            

    return answer