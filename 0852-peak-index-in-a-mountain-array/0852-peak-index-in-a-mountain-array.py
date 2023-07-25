class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        j = n - 1
        while i < j:
            m = i + (j - i) // 2
            if arr[m] < arr[m+1]:
                i = m + 1
            elif arr[m] < arr[m-1]:
                j = m - 1
            else:
                return m
        return i
