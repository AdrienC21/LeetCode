class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if hare == tortoise:
                break
        pointer1 = nums[0]
        pointer2 = tortoise
        while pointer1 != pointer2:
            pointer1 = nums[pointer1]
            pointer2 = nums[pointer2]
        return pointer1