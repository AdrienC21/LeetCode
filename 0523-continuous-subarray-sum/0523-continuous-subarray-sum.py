class Solution:
    # Okay, I had the good strat, not the right implementation:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}  # pairs cum sum mod k and index
        cum_sum = 0
        for i, n in enumerate(nums):
            cum_sum += n
            r = cum_sum % k
            if r not in dic:
                dic[r] = i
            elif i - dic[r] >= 2:
                return True
        return False
        
    # I tried something, but can't manage to fix the test case [0,1,0] with my strat
    # store only values mod k, put that in a set!
    # so O(n) complexity
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            if not(nums[i]) and not(nums[i+1]):
                return True
        if len(nums) <= 1:  # if one element or less, impossible
            return False
        nums = [x for x in nums if x != 0]  # remove individuals 0 (otherwise cum sum remains constant)
        cum_sum_mod = [nums[0] % k]
        for num in nums[1:]:
            cum_sum_mod.append((cum_sum_mod[-1] + num) % k)
        s = set()
        s.add(0)  # if the cum sum start at index 0
        s.add(cum_sum_mod[0])
        for elt in cum_sum_mod[1:]:
            if elt in s:
                return True
            s.add(elt)
        return False
    """
    # TLE O(n^2)
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 1:
            return False
        cum_sum = list(accumulate(nums))
        for i in range(-1, n-1):
            prev_sum = cum_sum[i] if i >= 0 else 0
            for j in range(i+2, n):
                if (cum_sum[j] - prev_sum) % k == 0:
                    return True
        return False
    """
