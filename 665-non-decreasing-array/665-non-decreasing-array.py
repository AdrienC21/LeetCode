class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        nb_bad_elements = 0
        i = 0
        while i < (n-1):
            if nums[i] > nums[i+1]:  # we need to modify one element
                nb_bad_elements += 1
                if i == 0:  # increase first element
                    nums[i] = nums[i+1]
                elif nums[i+1] >= nums[i-1]:  # [2,4,3], change 4 into 2
                    nums[i] = nums[i-1]
                else:  # [2,3,1], change 1 into 3
                    nums[i+1] = nums[i]
            else:
                i += 1
            if nb_bad_elements > 1:
                return False
        return True
