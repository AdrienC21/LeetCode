class Solution:
    """
    Note to future me:
    Astuce, le minimum c'est max(nums), le max c'est sum(nums) selon la valeur de m dans les deux extrêmes. Dichotomie pour tester la faisabilité d'une solution.
    Complexité: O(n*log(S)) où S=sum(nums)
    """
    def splitPossible(self, nums: List[int], m: int, mid: int):
        currentSum = 0
        nbSplit = 1  # we start with only 1 split
        for nb in nums:
            currentSum += nb
            if currentSum > mid:  # number nb starts a new split
                nbSplit += 1
                currentSum = nb
                if nbSplit > m:
                    return False
        return (nbSplit <= m)

    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        res = right  # first assume the answer is the worst scenario
        while left <= right:
            mid = left + ((right - left) // 2)  # avoid overflow
            if self.splitPossible(nums, m, mid):
                res = mid
                right = mid - 1  # the case of mid has already been tested so mid-1
            else:
                left = mid + 1
        return res