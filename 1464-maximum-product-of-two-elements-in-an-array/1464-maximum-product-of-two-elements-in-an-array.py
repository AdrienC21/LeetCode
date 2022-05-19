class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = None
        max2 = None
        for n in nums:
            if max1 is None:
                max1 = n
            elif max2 is None:
                if n > max1:
                    max1, max2 = n, max1
                else:
                    max2 = n
            elif n > max1:
                max1, max2 = n, max1
            elif n > max2:
                max2 = n
        return (max1 - 1) * (max2 - 1)