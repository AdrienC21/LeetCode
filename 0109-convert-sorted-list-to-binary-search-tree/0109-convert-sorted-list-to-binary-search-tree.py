# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_balanced_binary_tree(self, head: Optional[ListNode], i: int, j: int):
        if i > j:
            return None, head
        m = i + (j - i) // 2
        res = TreeNode()
        res.left, head = self.build_balanced_binary_tree(head, i, m - 1)
        res.val = head.val
        head = head.next
        res.right, head = self.build_balanced_binary_tree(head, m + 1, j)
        return res, head

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        root = head
        n = 0
        while root:
            n += 1
            root = root.next
        res, head = self.build_balanced_binary_tree(head, 0, n - 1)
        return res
