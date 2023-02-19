# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not(root):
            return res
        to_visit = [root]  # stack
        direction = 1  # 0 is to the left, 1 is to the right
        while to_visit:
            traversal = []
            next_to_visit = []
            if direction:
                for i in range(len(to_visit)):
                    traversal.append(to_visit[i].val)
                    if to_visit[i].left is not None:
                        next_to_visit.append(to_visit[i].left)
                    if to_visit[i].right is not None:
                        next_to_visit.append(to_visit[i].right)
            else:
                for i in range(len(to_visit)-1, -1, -1):
                    traversal.append(to_visit[i].val)
                    # right first now!
                    if to_visit[i].right is not None:
                        next_to_visit.append(to_visit[i].right)
                    if to_visit[i].left is not None:
                        next_to_visit.append(to_visit[i].left)
                next_to_visit = next_to_visit[::-1]  # reverse the nodes
            direction = 1 - direction  # change direction for the zigzag
            to_visit = next_to_visit  # update the next nodes to visit in this zigzag BFS
            res.append(traversal)  # add current traversal
        return res
