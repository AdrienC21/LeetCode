# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # perorder traversal: node left right
    # inorder traversal: left node right
    # not mine
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {inorder[i]: i for i in range(len(inorder))}  # hashmap to save time
        return self.recSearch(preorder, hashmap, 0, 0, len(preorder)-1)

    def recSearch(self, preorder: List[int], hashmap: Dict[int, int], root_index: int, left: int, right: int) -> TreeNode:
        # root_index, get the root, recursevely build the tree by extracting the correct index!
        rval = preorder[root_index]
        root, mid = TreeNode(rval), hashmap[rval]
        if mid > left:
            root.left = self.recSearch(preorder, hashmap, root_index+1, left, mid-1)
        if mid < right:
            root.right = self.recSearch(preorder, hashmap, root_index+mid-left+1, mid+1, right)
        return root
