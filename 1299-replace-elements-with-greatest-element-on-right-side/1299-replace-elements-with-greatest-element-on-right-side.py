from itertools import accumulate
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rev = arr[::-1]
        rev = list(accumulate(rev, max))
        arr[-1] = -1
        for i in range(1, len(arr)):
            arr[-(i+1)] = rev[i-1]
        return arr