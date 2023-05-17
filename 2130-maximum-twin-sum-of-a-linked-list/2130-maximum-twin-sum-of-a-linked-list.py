# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        L = []
        root = head
        while root:
            L.append(root.val)
            root = root.next
        n = len(L)
        res = -sys.maxsize
        for i in range(n // 2):
            res = max(res, L[i] + L[-(i+1)])
        return res
