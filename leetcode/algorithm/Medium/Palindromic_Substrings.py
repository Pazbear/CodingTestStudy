class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        len_s = len(s)
        for i in range(len_s):
            answer+=1
            for j in range(i+1, len_s):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    answer+=1
        return answer
                