class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])
        n = len(nums)
        for i in range(n-2):
            l = i + 1
            r = n - 1
            nbi = nums[i]
            while l < r:
                s = nbi + nums[l] + nums[r]
                if s == target:
                    return target
                elif s < target:
                    l += 1
                    if abs(target - s) < abs(target - closest):
                        closest = s
                else:
                    r -= 1
                    if abs(target - s) < abs(target - closest):
                        closest = s
        return closest
