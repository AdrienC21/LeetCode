class Solution:
    def sort(self, nums2, n, l) -> None:
        for j in range(l, n-1):
            if nums2[j] <= nums2[j+1]:
                break
            else:
                nums2[j], nums2[j+1] = nums2[j+1], nums2[j]
    def recMerge(self, nums1: List[int], m: int, k: int, nums2: List[int], n: int, l: int) -> None:
        if (n == 0) or (l == n):
            return
        elif (m == 0) or (k == m):
            for j in range(l, n):
                nums1[j-l+k] = nums2[j]
        elif nums1[k] <= nums2[l]:
            self.recMerge(nums1, m, k+1, nums2, n, l)
        else:
            nums1[k], nums2[l] = nums2[l], nums1[k]
            self.sort(nums2, n, l)
            self.recMerge(nums1, m, k+1, nums2, n, l)
            
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.recMerge(nums1, m, 0, nums2, n, 0)