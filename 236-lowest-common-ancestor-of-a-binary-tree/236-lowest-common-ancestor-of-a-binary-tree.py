# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recSearch(self, root: 'TreeNode', p: 'TreeNode'):
        if root is None:
            return [], False
        if root == p:
            return [], True
        l, b = self.recSearch(root.left, p)
        if b:
            return ["l"] + l, True
        r, b = self.recSearch(root.right, p)
        if b:
            return ["r"] + r, True
        return [], False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l_p, _ = self.recSearch(root, p)
        l_q, _ = self.recSearch(root, q)
        res = root
        i = 0
        while i < min(len(l_p), len(l_q)):
            if l_p[i] != l_q[i]:
                break
            if l_p[i] == "l":
                res = res.left
            else:
                res = res.right
            i += 1
        return res