from numpy.random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.shuffle_array = nums[:]
        self.len = len(nums)
    def reset(self) -> List[int]:
        self.shuffle_array = self.nums[:]
        return self.shuffle_array

    def shuffle(self) -> List[int]:
        for i in range(self.len-1, 0, -1):
            j = randint(0, i+1)
            self.shuffle_array[i], self.shuffle_array[j] = self.shuffle_array[j], self.shuffle_array[i]
        return self.shuffle_array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()