# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_depth(self, root: TreeNode) -> int:
        h = 0
        node = root
        while node.left:
            h += 1
            node = node.left
        return h
    
    def last_complete_layer(self, root: TreeNode, depth: int) -> List[TreeNode]:
        res = []
        def explore(root, h):
            nonlocal res, depth
            if not(root):
                return
            if h == 1:
                res.append(root)
                return
            explore(root.left, h-1)
            explore(root.right, h-1) 
        explore(root, depth)
        return res

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not(root):
            return 0
        depth = self.find_depth(root)
        if not(depth):
            return 1
        # h > 0
        layer = self.last_complete_layer(root, depth)  # h-1 nodes
        count = 2 ** depth - 1  # all the layers until the last
        for node in layer:
            if node.left:
                count += 1
            if node.right:
                count += 1
            else:
                break
        return count
