class Solution:
    def oneSum(self, nums: List[int], target: int, init_ind: int, init_val: int):
        for j, v in enumerate(nums):
            if (v + init_val) == target:
                return True, [init_ind, init_ind + 1 + j]
        return False, [0, 0]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            init_val = nums[i]
            (isSol, res) = self.oneSum(nums[i+1:], target, i, init_val)
            if isSol:
                return res
        return [0, 0]