class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return True
            elif nums[m] > nums[left]:
                if (target >= nums[left]) and (target < nums[m]):
                    right = m - 1
                else:
                    left = m + 1
            elif nums[m] < nums[left]:
                if (target > nums[m]) and (target <= nums[right]):
                    left = m + 1
                else:
                    right = m - 1
            else:
                left += 1  # due to the rotation, when nums[m] == nums[left] we have no conclusion
                
        return False