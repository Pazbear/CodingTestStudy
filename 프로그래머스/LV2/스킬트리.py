from collections import deque
import copy
def solution(skill, skill_trees):
    answer = 0
    skill = deque(skill)
    #skill_tree에서 skill에 해당하는 알파벳만 남김
    skill_trees = [[s for s in skill_tree if s in skill ] for skill_tree in skill_trees ]
    for skill_tree in skill_trees:
        temp = copy.deepcopy(skill)
        for s in skill_tree:
            if s == temp[0]:
                temp.popleft()
        if len(skill_tree)+len(temp) == len(skill): #기존 스킬트리의 스킬의 개수와 정해진 스킬에서 남은 개수가 정해진 스킬의 개수와 같을 때 = 스킬트리에서 스킬을 정확히 올렸을 경우 남는 알파벳이 없을때
            answer+=1
    return answer