# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # another approach using dfs
    # three states for the nodes:
    # 0, not monitored. 1, monitored. 2, has camera.
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cameras = 0
        def rec(root):
            nonlocal cameras
            if not(root):  # empty tree always monitored
                return 1
            left = rec(root.left)
            right = rec(root.right)
            if (left == 1) and (right == 1):  # children monitored, current node not
                return 0
            if not(left) or not(right):
                cameras += 1
                return 2
            return 1  # one of children has camera
        value_at_root = rec(root)  # call
        if not(value_at_root):  # root not monitored, add a camera
            cameras += 1
        return cameras
        
    # Brain melted, but I was almost there
    """
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # algorithm, return (a, b)
        # where a=nb of camera needed if there is a camera above the tree
        # b=nb of camera needed if there is no camera above the tree
        # (we place a camera at the root of the tree then)
        # therefore, we can calculate values for each node
        # finally the result can be calculated with minimums

        def rec(root: Optional[TreeNode]):
            if not(root):
                return (0, 0)
            (a1, b1) = rec(root.left)
            (a2, b2) = rec(root.right)
            # left: camera above, we don't place a camera so we need to cover the children. Three possibilities: we place two camera for the children, or one camera on the left and the right node is covered by its children, or the opposite.
            left = b1 + b2
            if a1:  # can cover left root with its children if left root has children
                left = min(left, 1 + a1 + b2)
            if a2:
                left = min(left, 1 + a2 + b1)
            if a1 and a2:
                left = min(left, 1 + a1 + a2)
            # right, no camera above. We place one camera (+1) and then we add the minimum number of cameras to cover the rest. One new possibilities, no camera for the children (a1+a2) as the two nodes are now covered.
            right = 1 + min(b1 + b2, a1 + b2, a2 + b1, a1 + a2)
            return (left, right)
        if not(root.left) and not(root.right):
            return 1
        if not(root.left):
            (a, b) = rec(root.right)
            return min(b, 1 + a)
        if not(root.right):
            (a, b) = rec(root.left)
            return min(b, 1 + a)
        (a1, b1) = rec(root.left)
        (a2, b2) = rec(root.right)
        res = b1 + b2  # camera children
        # camera root of the tree
        if a1:
            res = min(res, 1 + a1 + b2)
        if a2:
            res = min(res, 1 + a2 + b1)
        res = min(res, 1 + a1 + a2)
        return res
    """
