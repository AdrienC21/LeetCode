# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recMerge(self, L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:
        if L1 is None:
            return L2
        if L2 is None:
            return L1
        if L1.val <= L2.val:
            return ListNode(L1.val, self.recMerge(L1.next, L2))
        return ListNode(L2.val, self.recMerge(L2.next, L1))
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        L = [x for x in lists if not(x is None)]
        if not(L):
            return None
        L.sort(key=lambda x: x.val)
        while len(L) > 1:
            L1 = L.pop()
            L2 = L.pop()
            L.append(self.recMerge(L1, L2))
        return L[0]