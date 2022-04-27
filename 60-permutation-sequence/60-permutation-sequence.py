class Solution:
    # my function to calculate the next permutation
    def reverse(self, i: int, j: int, nums: List[int]) -> None:
        k = i
        l = j
        while k < l:
            nk = nums[k]
            nl = nums[l]
            nums[k], nums[l] = nl, nk
            k += 1
            l -= 1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i-1
                break
        if index == -1:
            self.reverse(0, n-1, nums)
            return None
        n_index = nums[index]
        for i in range(n-1, index, -1):
            if nums[i] > n_index:
                j = i
                break
        nums[i], nums[index] = n_index, nums[i]
        self.reverse(index+1, n-1, nums)
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        for _ in range(k-1):
            self.nextPermutation(nums)
        return "".join(map(lambda x: str(x), nums))