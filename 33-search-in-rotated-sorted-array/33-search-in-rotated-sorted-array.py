class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums)
        j = n - 1
        if nums[-1] < nums[0]:  # there is rotation
            if target < nums[0]:  # move i and regular binary search
                while (i < (n-1)) and (nums[i] <= nums[i+1]):
                    i += 1
                if i < (n-1):  # handle cases like [1]
                    i += 1
            else:  # move j and regular binary search
                while (j > 0) and (nums[j-1] <= nums[j]):
                    j -= 1
                if j > 0:  # handle cases like [1]
                    j -= 1
        while i < j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                j = m-1
            else:
                i = m+1
        if nums[i] == target:
            return i
        if nums[j] == target:
            return j
        return -1