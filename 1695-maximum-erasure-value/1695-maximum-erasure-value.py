class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        _set = set()  # set to have unique values
        n = len(nums)
        max_score = 0  # max sum of subarray elements
        running_score = nums[0]
        _set.add(nums[0])
        i = 1  # pointer
        start = 0  # start of the subarray
        while i < n:
            if nums[i] == nums[i-1]:
                max_score = max(max_score, running_score)
                running_score = nums[i]
                _set.clear()
                _set.add(nums[i])
                start = i
            elif nums[i] in _set:
                max_score = max(max_score, running_score)
                for j in range(start, i):
                    if nums[j] == nums[i]:
                        break
                    _set.discard(nums[j])
                    running_score -= nums[j]
                start = j + 1
            else:
                running_score += nums[i]
                _set.add(nums[i])
            i += 1
        max_score = max(max_score, running_score)
        return max_score
