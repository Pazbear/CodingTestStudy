# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        self.dfs(root)
        return root
    def dfs(self,node):
        if node == None:
            return
        node.left, node.right = node.right, node.left
        
        self.dfs(node.left)
        self.dfs(node.right)