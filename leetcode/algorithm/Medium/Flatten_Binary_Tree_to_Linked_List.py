# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return;
        dfs(root)
    
def dfs(root):
    if root.left:
        tmp = root.right
        lastLR = findLastLR(root.left)

        root.right = root.left
        root.left=None
        lastLR.right = tmp
    if not root.right:
        return
    dfs(root.right)
        
        
def findLastLR(root):
    if not root.right:
        return root
    else:
        return findLastLR(root.right)