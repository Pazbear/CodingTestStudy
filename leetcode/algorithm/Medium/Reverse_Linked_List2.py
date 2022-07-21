# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftnode, rightnode =head, head
        stop=False
        def recurse(rightnode, left, right):
            nonlocal leftnode, stop
            if right==1:
                return
            rightnode = rightnode.next
            if left>1:
                leftnode = leftnode.next
            recurse(rightnode, left-1, right-1)
            if leftnode==rightnode or rightnode.next == leftnode:
                stop=True
            if not stop:
                leftnode.val, rightnode.val = rightnode.val, leftnode.val
                leftnode=leftnode.next
        recurse(rightnode, left,right)
        return head