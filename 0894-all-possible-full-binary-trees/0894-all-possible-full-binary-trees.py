# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.cache = {1: [TreeNode(0)]}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if (n % 2) == 0:
            return []
        if n in self.cache:
            return self.cache[n]
        res = []
        for k in range(1, ((n - 1) // 2), 2):
            sub_res_1 = self.allPossibleFBT(k)
            sub_res_2 = self.allPossibleFBT(n-1-k)
            for t1 in sub_res_1:
                for t2 in sub_res_2:
                    res.append(TreeNode(0, left=t1, right=t2))
                    res.append(TreeNode(0, left=t2, right=t1))
        sub_res_3 = self.allPossibleFBT((n - 1) // 2)
        for t1 in sub_res_3:
            for t2 in sub_res_3:
                res.append(TreeNode(0, left=t1, right=t2))
        self.cache[n] = res
        return res
