import numpy as np
class Solution:
    def is_sorted(self, s: List[str]) -> bool:
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                return False
        return True

    def minDeletionSize(self, strs: List[str]) -> int:
        strs_array = np.array([list(s) for s in strs])
        to_remove = 0
        for j in range(len(strs_array[0])):
            if not(self.is_sorted(strs_array[:,j])):
                to_remove += 1
        return to_remove
