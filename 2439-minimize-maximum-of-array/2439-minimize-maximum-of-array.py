class Solution:
    def ceil(self, n: float) -> int:
        if n == int(n):
            return int(n)
        return int(n) + 1

    # flow goes to the left, max of all the averages
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        running_sum = nums[0]
        for i in range(1, len(nums)):
            running_sum += nums[i]
            res = max(res, self.ceil(running_sum / (i+1)))
        return res

    # WRONG APPROACH
    # best flow is gonna spread the mean for each increasing sequence
    # => calculate all the means and return the max
    """
    def minimizeArrayValue(self, nums: List[int]) -> int:
        current_max = -sys.maxsize
        i = 1
        n = len(nums)
        running_avg = nums[0]
        running_count = 1
        while i < n:
            if nums[i] >= nums[i-1]:
                running_count += 1
                running_avg = running_avg + (nums[i] - running_avg) / running_count
            else:
                current_max = max(current_max, running_avg)
                running_avg = nums[i]
                running_count = 1
            i += 1
        current_max = max(current_max, running_avg)
        if current_max == int(current_max):
            return int(current_max)
        return int(current_max) + 1
    """
