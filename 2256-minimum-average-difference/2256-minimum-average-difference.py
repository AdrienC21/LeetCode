from itertools import accumulate
import numpy as np
class Solution:
    # O(n)
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        avg_left = list(accumulate(nums))
        for i in range(1, n+1):
            avg_left[i-1] = avg_left[i-1] / i
        avg_left = np.array(avg_left)

        avg_right = list(accumulate(nums[::-1]))
        for i in range(1, n+1):
            avg_right[i-1] = avg_right[i-1] / i
        avg_right.pop()
        avg_right = [0] + avg_right
        avg_right = np.array(avg_right[::-1])

        min_index = n
        val = sys.maxsize
        for i in range(n):
            if abs(int(avg_left[i]) - int(avg_right[i])) < val:
                val = abs(int(avg_left[i]) - int(avg_right[i]))
                min_index = i
        return min_index

    # floating error on [99999] + 99999 * [0]
    """
    def minimumAverageDifference(self, nums: List[int]) -> int:
        avg_left = [nums[0]]
        avg_right = [nums[-1]]
        n = len(nums)
        for i in range(1, n):
            avg_left.append((i*avg_left[-1] + nums[i]) / (i+1))
            avg_right.append((i*avg_right[-1] + nums[-(i+1)]) / (i+1))
        avg_right = [0] + avg_right  # add mean of 0 element
        avg_right.pop()  # remove mean of n elements
        avg_right = avg_right[::-1]  # reverse
        avg_left = [int(x) for x in avg_left]
        avg_right = [int(x) for x in avg_right]

        # search min index
        min_index = n
        val = sys.maxsize
        for i in range(n):
            if abs(avg_left[i] - avg_right[i]) < val:
                val = abs(avg_left[i] - avg_right[i])
                min_index = i
        return min_index
    """
