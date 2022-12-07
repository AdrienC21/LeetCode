# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recmod(self, head: Optional[ListNode]):
        if head is None:
            return None, None
        if head.next is None:
            return head, head
        if head.next.next is None:
            return head, head
        root1, root2 = self.recmod(head.next.next)
        head.next.next = root2.next
        root2.next = head.next
        head.next = root1
        return head, root2
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res, _ = self.recmod(head)
        return res
