class Solution:
    def calcMax(self, res1: List[int], res2: List[int]) -> int:
        diff_idx = res2[0] - res1[0]
        diff_h = res2[1] - res1[1]
        if diff_h >= 0:
            diff = diff_idx - diff_h  # we first egalize the size, then draw a parabola to reach max high
            return max(res1[1], res2[1]) + (diff // 2)
        diff = diff_idx + diff_h
        return max(res1[1], res2[1]) + (diff // 2)
        
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        new_res = [[0, 0]] + [[x[0]-1, x[1]] for x in restrictions]
        new_res.sort(key=lambda x: x[0])
        
        # update the restrictions to reachable sizes (restriction due to height difference)
        for i in range(len(new_res)-1):
            new_res[i+1][1] = min(new_res[i+1][1], new_res[i][1]+(new_res[i+1][0]-new_res[i][0]))

        for i in range(len(new_res)-1, 0, -1):
            new_res[i-1][1] = min(new_res[i-1][1], new_res[i][1] + (new_res[i][0] - new_res[i-1][0]))

        maximum = 0
        for i in range(len(new_res)-1):
            max_i = self.calcMax(new_res[i], new_res[i+1])
            maximum = max(maximum, max_i)
        nb_remaining_building = n - new_res[-1][0] - 1
        max_last = nb_remaining_building + new_res[-1][1]
        maximum = max(maximum, max_last)
        return maximum
