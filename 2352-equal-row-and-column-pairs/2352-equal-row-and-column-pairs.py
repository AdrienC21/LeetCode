import numpy as np


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        for row in grid:
            hashmap[",".join([str(x) for x in row])] += 1
        res = 0
        for col in np.transpose(grid):
            res += hashmap[",".join([str(x) for x in col])]
        return res
