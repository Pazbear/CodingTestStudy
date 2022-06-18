from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer=[]
        len_p=len(p)
        if len_p > len(s): # p가 s보다 길면 anagram은 없음
            return answer
        
        setp= defaultdict(int)
        for elem_p in p:
            setp[elem_p]+=1
            
        for i in range(0, len_p):
            setp[s[i]]-=1
        if self.isSame(setp):
            answer.append(0)
        for i in range(1,len(s)-len_p+1):
            setp[s[i-1]]+=1
            setp[s[i+len_p-1]]-=1
            if self.isSame(setp):
                answer.append(i)
        return answer
    def isSame(self, setp): ## setp의 원소가 모두 0일경우 p와 현재 인덱스의 s가 같음을 알수 있음
        for elem_p in setp:
            if setp[elem_p] != 0:
                return False
        return True