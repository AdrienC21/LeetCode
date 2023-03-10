import numpy as np

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        root = head
        self.len = 0
        while root:
            self.len += 1
            root = root.next

    def getRandom(self) -> int:
        i = np.random.randint(0, self.len)
        root = self.head
        while i:
            root = root.next
            i -= 1
        return root.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()