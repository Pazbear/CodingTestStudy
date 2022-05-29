class Solution:
    not_possible = False
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        answer=[]
        visited=[0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            a, b = prerequisite
            graph[b].append(a)

        for i in range(numCourses):
            if visited[i]==0:
                self.dfs(graph,i,visited, answer)
        return answer[::-1] if not self.not_possible else []
 

    def dfs(self,graph,curr,visited, answer):
        if self.not_possible:
            return

        visited[curr]=2
        for next in graph[curr]:
            if visited[next]==0:
                self.dfs(graph, next,visited, answer)
            elif visited[next]==2:
                self.not_possible = True
        visited[curr]=1
        answer.append(curr)