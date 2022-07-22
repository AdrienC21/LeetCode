# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = []
        right = []
        while head:
            if head.val < x:
                left.append(head.val)
            else:
                right.append(head.val)
            head = head.next
        res = None
        while right:
            res = ListNode(val=right.pop(), next=res)
        while left:
            res = ListNode(val=left.pop(), next=res)
        return res
