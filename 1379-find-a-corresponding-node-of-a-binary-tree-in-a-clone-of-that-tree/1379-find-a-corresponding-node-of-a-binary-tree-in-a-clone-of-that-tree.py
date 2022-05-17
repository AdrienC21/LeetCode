# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        decisions = []
        def recSearch(tree, target):
            nonlocal decisions
            if tree:
                if tree == target:
                    return True
                left = recSearch(tree.left, target)
                if left:
                    decisions.append("left")
                    return True
                right = recSearch(tree.right, target)
                if right:
                    decisions.append("right")
                    return True
            return False
        recSearch(original, target)
        n = cloned
        while decisions:
            side = decisions.pop()
            if side == "left":
                n = n.left
            else:
                n = n.right
        return n