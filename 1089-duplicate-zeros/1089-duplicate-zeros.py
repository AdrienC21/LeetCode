class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        cop = arr[:]
        n = len(arr)
        i = 0
        j = 0
        while (i < n) and (j < n):
            arr[i] = cop[j]
            if arr[i] == 0:
                i += 1
                if i < n:
                    arr[i] = 0
            i += 1
            j += 1