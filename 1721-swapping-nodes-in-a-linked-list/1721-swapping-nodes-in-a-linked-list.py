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
    # V2
    """
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        root = head
        n = 0
        while root:
            root = root.next
            n += 1
        kfirst = head
        klast = head
        count = k
        while count > 1:
            kfirst = kfirst.next
            count -= 1
        count = 0
        while count < (n - k):
            klast = klast.next
            count += 1
        kfirst.val, klast.val = klast.val, kfirst.val
        return head
    """
