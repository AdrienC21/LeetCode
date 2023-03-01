# Other possible solutions include:
# - in place merge sort
# - Implement the heap structure and heapify
import random


class Solution:
    def is_sorted(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True

    def is_rev_sorted(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                return False
        return True

    # Quicksort in place
    def sortArray(self, nums: List[int]) -> List[int]:
        # Check some scenario where quicksort is O(n^2) first
        if self.is_sorted(nums):
            return nums
        if self.is_rev_sorted(nums):
            return nums[::-1]

        def partition(i: int, j: int) -> int:
            # better with random initial position
            rand_pivot_pos = random.randint(0, j - i) + i
            # place it at the end
            nums[rand_pivot_pos], nums[j] = nums[j], nums[rand_pivot_pos]
            pivot = nums[j]
            k = i  # position where the pivot should end
            for i in range(i, j):
                if nums[i] <= pivot:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1
            nums[k], nums[j] = nums[j], nums[k]
            return k  # position of the pivot

        def quicksort(i: int, j: int) -> None:
            if j <= i:
                return None
            k = partition(i, j)
            quicksort(i, k-1)
            quicksort(k+1, j)
        
        quicksort(0, len(nums) - 1)
        return nums
