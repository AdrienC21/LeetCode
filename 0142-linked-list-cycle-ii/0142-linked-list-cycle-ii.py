# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        head.prev = None
        while head:
            if head.next is None:
                return None
            if "prev" in head.next.__dir__():  # then head.next beginning of cycle
                return head.next
            # else, update next and move to next
            head.next.prev = head
            head = head.next
