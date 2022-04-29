class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        while (i < n) and (j < n):
            if nums[i] == val:
                if nums[j] == val:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1
        return i