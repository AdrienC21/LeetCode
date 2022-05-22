class Solution:
    # O(n^2) with two pointers
    def triangleNumber(self, nums: List[int]) -> int:
        if not(nums) or len(nums) < 3:
            return 0
        nums.sort()
        res = 0
        for i in range(len(nums)-1, 1, -1):
            l = 0  # pointers
            r = i - 1
            while l < r:
                if nums[i] < (nums[l] + nums[r]):
                    res += r - l  # with r fixed, we have l-r triangles
                    r -= 1  # decrease r
                else:
                    l += 1  # need to increase l for larger sum of two sides

        return res
        
    # Brute force, O(n^3) more or less, but TLE
    """
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                two_sides = nums[i] + nums[j]
                for k in range(j+1, n):
                    if nums[k] >= two_sides:
                        break
                    res += 1
        return res
    """
