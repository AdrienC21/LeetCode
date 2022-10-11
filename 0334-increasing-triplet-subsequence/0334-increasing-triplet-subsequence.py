class Solution:
    # O(n) !!
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = sys.maxsize
        second_largest = sys.maxsize
        for nb in nums:
            if nb <= smallest:
                smallest = nb
            elif nb <= second_largest:
                second_largest = nb
            else:
                return True
        return False
    # TLE
    """
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < (n-2):
            j = i + 1
            if nums[j] <= nums[i]:
                i += 1
            else:
                while (j < (n-1)) and (nums[j] > nums[i]):
                    for k in range(j+1, n):
                        if nums[k] > nums[j]:
                            return True
                    j += 1
                i += 1
        return False
    """
