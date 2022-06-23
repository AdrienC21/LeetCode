class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        L = []
        len_L = 0
        for n in nums:
            if len_L < k:
                L.append(n)
                len_L += 1
                i = len_L - 1
                while (i > 0) and (L[i] > L[i-1]):
                    L[i], L[i-1] = L[i-1], L[i]
                    i -= 1
            elif n > L[-1]:
                L.pop()
                L.append(n)
                i = k - 1
                while (i > 0) and (L[i] > L[i-1]):
                    L[i], L[i-1] = L[i-1], L[i]
                    i -= 1
        return L[-1]
