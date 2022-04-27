# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = [None]
        first = [None]
        middle = [None]
        last = [None]
        
        def recSearch(root: Optional[TreeNode], prev: Optional[TreeNode],
                      first: Optional[TreeNode], middle: Optional[TreeNode],
                      last: Optional[TreeNode]) -> None:
            if root:
                recSearch(root.left, prev, first, middle, last)
                
                if prev[0] and (root.val < prev[0].val):
                    if not(first[0]):
                        first[0] = prev[0]
                        middle[0] = root
                    else:
                        last[0] = root

                prev[0] = root

                recSearch(root.right, prev, first, middle, last)
            
        recSearch(root, prev, first, middle, last)
        
        if first[0] and last[0]:
            first[0].val, last[0].val = last[0].val, first[0].val

        elif first[0] and middle[0]:
            first[0].val, middle[0].val = middle[0].val, first[0].val