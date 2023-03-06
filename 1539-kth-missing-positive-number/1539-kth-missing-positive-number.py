class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        current_nb = 1
        i = 0  # pointer in arr
        n = len(arr)
        while i < n:
            if arr[i] != current_nb:
                count += 1
                if count == k:
                    return current_nb
            else:
                i += 1
            current_nb += 1
        return current_nb + (k - count - 1)
