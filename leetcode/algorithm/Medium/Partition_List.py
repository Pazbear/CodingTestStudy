# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_node, greater_node = ListNode(0), ListNode(0)
        less_head, greater_head = less_node, greater_node
        while head:
            if head.val < x:
                less_node.next = head
                less_node = less_node.next
            else:
                greater_node.next = head
                greater_node = greater_node.next
            head = head.next
        greater_node.next = None
        less_node.next = greater_head.next
        return less_head.next