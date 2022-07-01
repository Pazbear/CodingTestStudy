class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer=[]
        start = dict()
        end = dict()
        for i in range(len(s)):
            if s[i] not in start:
                start[s[i]]=i
            if s[i] not in end:
                end[s[i]]=i
            else:
                end[s[i]]=i
        sorted_start = dict(sorted(start.items(), key=lambda x : x[1]))
        index =0
        prev = 0 
        for st in sorted_start:
            if sorted_start[st] <=index:
                index = max(index, end[st])
            else:
                if not answer:
                    answer.append(index+1)
                    prev = index
                else:
                    answer.append(index-prev)
                prev = index
                index = end[st]
        if not answer:
            return [len(s)]
        else:
            answer.append(len(s)-1-prev)
            return answer