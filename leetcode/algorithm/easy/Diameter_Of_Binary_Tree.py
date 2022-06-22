# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def circuit(root, cnt):
            if root == None:
                return 0
            left = circuit(root.left, cnt+1)
            right = circuit(root.right, cnt+1)

            if self.answer < left+right:
                self.answer = left+right
            return max(left, right)+1
        circuit(root, 0)
        return self.answer