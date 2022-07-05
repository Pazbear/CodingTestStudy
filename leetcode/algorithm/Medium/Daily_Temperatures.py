class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[]
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:#이전보다 큰 수가 나올 때마다 처리
                prev = stack.pop()
                answer[prev]=i-prev
            stack.append(i)
        return answer