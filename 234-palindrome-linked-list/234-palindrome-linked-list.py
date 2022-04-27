# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listNodeToStr(self, head: Optional[ListNode]) -> list:
        if head.next is None:
            return str(head.val)
        else:
            return str(head.val) + self.listNodeToStr(head.next)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = self.listNodeToStr(head)
        
        return (s == s[::-1])
        