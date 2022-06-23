class Solution:
    # TIPS! Best solution (not mine): variation of quicksort: quickselect. worst O(n^2) but on average O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        stop_pos = n - k  # position of the k largest element in a sorted array
        def quickSelect(l, r):
            pivot_val, pointer = nums[r], l  # rightmost value as a pivot
            for i in range(l, r):
                if nums[i] <= pivot_val:
                    nums[pointer], nums[i] = nums[i], nums[pointer]  # move the item to the left part of the array
                    pointer += 1
            nums[pointer], nums[r] = nums[r], nums[pointer]  # move the pivot to the last pointer position
            if pointer > stop_pos:  # k largest element is before the pointer
                return quickSelect(l, pointer - 1)
            elif pointer < stop_pos:  # k largest element is after the pointer
                return quickSelect(pointer + 1, r)
            else:
                return nums[pointer]
        return quickSelect(0, n - 1)
    
    # building a heap: O(n). Proof here: https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/?ref=lbp
    # so solution, heap, remove k-1 elements. O(n+k*log(n))
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [-n for n in nums]  # convert to negative value because heapq only min heap and we want max heap
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)  # pop k-1 smallest (k-1 largest after multiplying by -1)
        return -nums[0]        
    """
    
    # sorting the array: nlog(n)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
    """
    
    # list of k largest elements
    # worst case: O(k*n), best case: O(n)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        L = []
        len_L = 0
        for n in nums:
            if len_L < k:
                L.append(n)
                len_L += 1
                i = len_L - 1
                while (i > 0) and (L[i] > L[i-1]):
                    L[i], L[i-1] = L[i-1], L[i]
                    i -= 1
            elif n > L[-1]:
                L.pop()
                L.append(n)
                i = k - 1
                while (i > 0) and (L[i] > L[i-1]):
                    L[i], L[i-1] = L[i-1], L[i]
                    i -= 1
        return L[-1]
    """
