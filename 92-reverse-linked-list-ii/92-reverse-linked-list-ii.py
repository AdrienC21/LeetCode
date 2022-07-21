# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = head
        while left > 1:
            root = root.next
            left -= 1
            right -= 1
        # left == 1
        d = []
        root2 = root
        d.append(root.val)
        while right > 1:
            root2 = root2.next
            d.append(root2.val)
            right -= 1
        while d:
            root.val = d.pop()
            root = root.next
        return head
