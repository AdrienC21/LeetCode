# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lenLinkedList(self, head: Optional[ListNode]) -> int:
        root = head
        count = 0
        while root:
            count += 1
            root = root.next
        return count

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k = self.lenLinkedList(head) // 2  # k = n // 2
        if k == 0:
            return None
        root = head
        while k > 1:
            root = root.next
            k -= 1
        root.next = root.next.next
        return head
