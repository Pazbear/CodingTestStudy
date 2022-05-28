from collections import deque
def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    visited=[0 for _ in range(len(info))]
    used=[0 for _ in range(len(info))]
    used[0]=1
    return dfs(info, graph, 0, visited,used, 1, 0)

def dfs(info, graph,node, visited,used, sheep, wolf):
    visited[node] = 1
    res=0
    for line in graph[node]:
        if visited[line] != 0:
            continue
                
        if info[line] ==1 and sheep > wolf+1:
            if used[line]==0:
                used[line]=1
                res=dfs(info, graph, line, visited,used, sheep, wolf+1)
                used[line]=0
            else:
                res=dfs(info, graph, line, visited,used, sheep, wolf)
        elif info[line]==0:
            if used[line]==0:
                used[line]=1
                resetVisited(visited)
                visited[line]=1
                res=dfs(info, graph, line, visited,used, sheep+1, wolf)
                used[line]=0
            else:
                res=dfs(info, graph, line, visited,used, sheep, wolf)
    return max(res,sheep)
            
def resetVisited(visited):
    for i in range(len(visited)):
        visited[i]=0