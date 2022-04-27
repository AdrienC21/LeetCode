# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodeToNb(self, l) -> int:
        if l is None:
            return 0
        else:
            return l.val + 10 * self.nodeToNb(l.next)
    def nbToNode(self, s):
        if s == "":
            return None
        else:
            return ListNode(int(s[0]), self.nbToNode(s[1:]))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.nodeToNb(l1)
        n2 = self.nodeToNb(l2)
        return self.nbToNode(str(n1 + n2)[::-1])