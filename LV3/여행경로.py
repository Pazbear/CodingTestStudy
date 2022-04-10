def solution(tickets):
    answer = []
    stopby = [0 for _ in range(len(tickets))]
    path = ['ICN']
    answer=[]
    tickets = sorted(tickets, key=lambda x : x[1])
    return dfs(tickets, path, stopby)
    

def dfs(tickets, path, stopby):
    if len(tickets)+1 == len(path):
        return path
    for i in range(len(tickets)):
        if stopby[i]==0 and tickets[i][0] == path[-1]:
            stopby[i]=1
            path.append(tickets[i][1])
            temp = dfs(tickets, path, stopby)
            if temp != None:
                return temp
            path.pop()
            stopby[i]=0