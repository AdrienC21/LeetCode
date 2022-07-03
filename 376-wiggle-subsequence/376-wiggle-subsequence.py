class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            return 1
        count = 1
        increasing = None
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if increasing is None:
                    if nums[i] < nums[i-1]:
                        increasing = False
                    else:
                        increasing = True
                if increasing:
                    if nums[i] > nums[i-1]:
                        increasing = False
                        count += 1
                else:
                    if nums[i] < nums[i-1]:
                        increasing = True
                        count += 1
        return count
