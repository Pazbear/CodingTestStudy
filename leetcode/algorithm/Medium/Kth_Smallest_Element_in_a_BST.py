# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        self.circuit(root, heap)
        for i in range(1,k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
    def circuit(self,node, heap):
        if node == None:
            return
        
        heapq.heappush(heap, node.val)
        self.circuit(node.left, heap)
        self.circuit(node.right, heap)