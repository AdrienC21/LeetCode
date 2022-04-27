# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k = k - 1
        firstNode = head
        while k > 0:
            firstNode = firstNode.next
            k -= 1
        
        f = firstNode
        secondNode = head
        
        while not(f.next is None):
            f = f.next
            secondNode = secondNode.next
        
        val1 = firstNode.val
        val2 = secondNode.val
        firstNode.val = val2
        secondNode.val = val1
        
        return head