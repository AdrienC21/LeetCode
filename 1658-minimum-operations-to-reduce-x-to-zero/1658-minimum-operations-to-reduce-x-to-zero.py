class Solution:
    # Sliding window
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)
        
        if target == 0:
            return n
        
        left = 0
        right = 0 
        running_sum = 0
        nb_elt = 0 
        
        while right < n:
            running_sum = running_sum + nums[right]
            
            while left < right and running_sum > target:
                running_sum = running_sum - nums[left]
                left = left + 1
            if running_sum == target:
                nb_elt = max(nb_elt, right - left + 1)  # max target to min nb operations
            right = right + 1
            
        if nb_elt == 0:
            return -1 
        else:
            return n - nb_elt 
    # recursive, but time limit exceeded :/
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        if not(nums):
            return -1
        if len(nums) == 1:
            if nums[0] == x:
                return 1
            return -1
        if (nums[0] == x) or (nums[-1] == x):
            return 1
        if nums[0] > x:
            if nums[-1] > x:
                return -1
            sub = self.minOperations(nums[1:-1], x-nums[-1])
            if sub != -1:
                return sub + 1
            return sub
        if nums[-1] > x:
            sub = self.minOperations(nums[1:-1], x-nums[0])
            if sub != -1:
                return sub + 1
            return sub
        sub_left = self.minOperations(nums[1:], x-nums[0])
        sub_right = self.minOperations(nums[:-1], x-nums[-1])
        if sub_left == -1:
            if sub_right == -1:
                return -1
            return sub_right + 1
        if sub_right == -1:
            return sub_left + 1
        return min(sub_left, sub_right) + 1
    """
