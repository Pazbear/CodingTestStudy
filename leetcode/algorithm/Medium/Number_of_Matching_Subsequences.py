from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        answer=0
        dic = defaultdict(list)
        for i, c in enumerate(s):
            dic[c].append(i)
        for word in words:
            prev = -1
            for i,word_elem in enumerate(word):
                foundIndex=False
                for index in dic[word_elem]:
                    if index>prev:
                        prev=index
                        foundIndex=True
                        break
                if not foundIndex:
                    break
                if foundIndex and i == len(word)-1:
                    answer+=1
        return answer