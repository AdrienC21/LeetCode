# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        current_path = []
        def recSearch(root: Optional[TreeNode], current_sum: int) -> None:
            nonlocal current_path, targetSum
            if not(root):
                return
            if not(root.left) and not(root.right):
                if current_sum + root.val == targetSum:
                    current_path.append(root.val)
                    paths.append(current_path[:])
                    current_path.pop()
                return
            current_path.append(root.val)
            current_sum += root.val
            if root.left:
                recSearch(root.left, current_sum)
            if root.right:
                recSearch(root.right, current_sum)  
            current_path.pop()
            current_sum -= root.val
        recSearch(root, 0)
        return paths
