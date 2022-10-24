class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        res = [0, 0]
        for num in nums:
            if num in s:  # in double
                res[0] = num
            s.add(num)
        for i in range(1, len(nums)+1):
            if i not in s:
                res[1] = i
                break
        return res
