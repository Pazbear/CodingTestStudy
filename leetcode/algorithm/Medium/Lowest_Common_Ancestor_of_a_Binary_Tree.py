# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = []
        self.circuit(root, p.val, q.val, answer)
        return TreeNode(answer[0])
    
    def circuit(self, node, p, q, answer):
        if node == None:
            return False
        #왼쪽에 값이 있는지
        res1 = self.circuit(node.left, p, q, answer)
        #오른쪽에 값이 있는지
        res2 = self.circuit(node.right, p, q, answer)
        #현재 값이 원하는 값인지
        curr = node.val==p or node.val==q
        
        if res1 and res2:
            answer.append(node.val)
            return False
        elif (res1 and curr) or (res2 and curr):
            answer.append(node.val)
            return False
        elif curr:
            return True
        elif res1 or res2:
            return True
        else:
            return False