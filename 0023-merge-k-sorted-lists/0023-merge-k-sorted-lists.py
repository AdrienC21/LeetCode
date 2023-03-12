# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            return ListNode(l1.val, self.mergeLists(l1.next, l2))
        if l1.val == l2.val:
            return ListNode(l1.val, ListNode(l2.val, self.mergeLists(l1.next, l2.next)))
        return ListNode(l2.val, self.mergeLists(l1, l2.next))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not(lists):
            return None
        lists = sorted(lists, key=lambda x: x.val if x is not None else sys.maxsize)
        while len(lists) > 1:
            l2 = lists.pop()
            l1 = lists.pop()
            lists.append(self.mergeLists(l1, l2))            
        return lists[0]
