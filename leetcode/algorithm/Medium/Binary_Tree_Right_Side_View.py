# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        answer = []
        self.circuit(root, answer)
        return answer
    def circuit(self, root, answer):
        queue = deque()
        queue.append((root, 0))
        while queue:
            curr, level = queue.popleft()
            if len(answer)==level:
                answer.append(curr.val)
            if curr.right:
                queue.append((curr.right, level+1))
            if curr.left:
                queue.append((curr.left, level+1))
                
        