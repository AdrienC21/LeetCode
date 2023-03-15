# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # calculate height of the tree
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    # if before reaching max_h - 1 level, we encounter a None, return False
    # return the values of the last level
    def get_node_last_h(self, root: Optional[TreeNode], h: int, max_h: int) -> Tuple[bool, List[int]]:
        if (root is None) and (h < max_h):
            return False, []
        if h == (max_h - 1):
            if (root.left is None) and not(root.right is None):
                return False, []
            if root.left is None:
                return True, [None, None]
            if root.right is None:
                return True, [root.left.val, None]
            return True, [root.left.val, root.right.val]
        left_b, left_l = self.get_node_last_h(root.left, h+1, max_h)
        if not(left_b):
            return False, []
        right_b, right_l = self.get_node_last_h(root.right, h+1, max_h)
        if not(right_b):
            return False, []
        l = left_l + right_l
        return True, l
    
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        max_h = self.height(root)
        if not(max_h):
            return True
        b, l = self.get_node_last_h(root, 0, max_h)
        if not(b):
            return False
        # return False if we see values -> None -> values at the last layer
        while l and (l[-1] is None):
            l.pop()
        if None in l:
            return False
        return True
