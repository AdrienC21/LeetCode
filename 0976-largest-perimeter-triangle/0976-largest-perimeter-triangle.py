class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            if nums[i-2] > (nums[i] - nums[i-1]):
                return nums[i-2] + nums[i-1] + nums[i]
        return 0
    # TLE: would be great for max area, but for perimeter of course it's easier ...
    """
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        max_perimeter = 0
        for i in range(n-2):
            a = nums[i]
            for j in range(i+1, n-1):
                b = nums[j]
                if (a, b) not in seen:
                    seen.add((a, b))
                    seen.add((b, a))
                    diff = max(a, b) - min(a, b)
                    add = a + b
                    for k in range(j+1, n):
                        c = nums[k]
                        if (c > diff) and (c < add):
                            max_perimeter = max(max_perimeter, add + c)
        return max_perimeter
    """
