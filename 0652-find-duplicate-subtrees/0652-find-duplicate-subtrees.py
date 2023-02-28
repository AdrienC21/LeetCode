# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        s = set()
        duplicates = []

        def root_equal(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
            if not(r1) and not(r2):
                return True
            if r1 and not(r2):
                return False
            if r2 and not(r1):
                return False
            if r1.val != r2.val:
                return False
            return root_equal(r1.left, r2.left) and root_equal(r1.right, r2.right)

        def recSearch(root: Optional[TreeNode]) -> str:
            nonlocal s, duplicates

            if not(root):
                return " "
            left = recSearch(root.left)
            right = recSearch(root.right)
            h = f"l_{left}_{root.val}_r_{right}"
            if h in s:  # duplicate
                for r in duplicates:
                    if root_equal(r, root):
                        break
                else:  # add it
                    duplicates.append(root)
            else:
                s.add(h)
            return h

        recSearch(root)
        return duplicates
