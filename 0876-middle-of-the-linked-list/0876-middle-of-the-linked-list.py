# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        length = 1
        while root.next:
            root = root.next
            length += 1
        k = (length // 2)
        root = head
        while k:
            k -= 1
            root = root.next
        return root
