# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not(inorder) or not(postorder):
            return None
        # find top value of the tree
        top_val = postorder[-1]
        # find the left part of the tree
        for size_left_tree in range(len(inorder)):
            if inorder[size_left_tree] == top_val:
                break
        # create recursively the left and right tree
        if not(size_left_tree):
            left_part = None
            right_part = self.buildTree(inorder[1:], postorder[:-1])
        if size_left_tree == len(inorder):
            left_part = self.buildTree(inorder[:size_left_tree], postorder[:size_left_tree])
            right_part = None
        else:
            left_part = self.buildTree(inorder[:size_left_tree], postorder[:size_left_tree])
            right_part = self.buildTree(inorder[size_left_tree+1:], postorder[size_left_tree:-1])
        # merge
        return TreeNode(top_val, left_part, right_part)
