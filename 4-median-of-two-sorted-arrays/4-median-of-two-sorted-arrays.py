class Solution:
    """
    # works but doesn't give 3 in the case below (it gives 2 :/)
    # [2,2,4,4]
    # [2,2,4,4]
    
    def med2(self, a: int, b: int) -> float:
        return (a + b) / 2
    def med3(self, a: int, b: int, c: int) -> float:
        return a + b + c - max(a, max(b, c)) - min(a, min(b, c))
    def med4(self, a: int, b: int, c: int, d: int) -> float:
        return (a + b + c + d - max(a, max(b, max(c, d))) - min(a, min(b, min(c, d)))) / 2
    def medList(self, L: List[int], size: int) -> float:
        if size == 0:
            return -1
        elif size == 1:
            return L[0]
        elif size % 2 == 0:
            return (L[size//2 - 1] + L[size//2]) / 2
        else:
            return L[size//2]
    def recMedian(self, nums1: List[int], s1: int, nums2: List[int], s2: int) -> float:
        if s2 < s1:
            return self.recMedian(nums2, s2, nums1, s1)
        elif s1 == 0:
            return self.medList(nums2, s2)
        elif s1 == 1:
            if s2 == 1:
                return self.med2(nums1[0], nums2[0])
            elif s2 % 2 == 1:
                return self.med2(nums2[s2//2], self.med3(nums1[0], nums2[s2//2 - 1], nums2[s2//2 + 1]))
            else:
                return self.med3(nums1[0], nums2[s2//2 - 1], nums2[s2//2])
        elif s1 == 2:
            if s2 == 2:
                return self.med4(nums1[0], nums1[1], nums2[0], nums2[1])
            elif s2 % 2 == 1:
                return self.med3(nums2[s2//2], max(nums1[0], nums2[s2//2 - 1]), min(nums1[1], nums2[s2//2 + 1]))
            else:
                return self.med4(nums2[s2//2 - 1], nums2[s2//2], max(nums1[0], nums2[s2//2 - 2]), min(nums1[1], nums2[s2//2 + 1]))
        else:
            m1 = (s1 - 1) // 2
            m2 = (s2 - 1) // 2
            if nums1[m1] <= nums2[m2]:
                return self.recMedian(nums1[m1:], s1 - m1, nums2[:m2+1], m2 + 1)
            return self.recMedian(nums1[:m1+1], m1 + 1, nums2[m2:], s2 - m2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)
        if size1 <= size2:
            return self.recMedian(nums1, size1, nums2, size2)
        return self.recMedian(nums2, size2, nums1, size1)
    """
    
    # binary search
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s1 = len(nums1)
        s2 = len(nums2)
        if (s1 > s2):
            return self.findMedianSortedArrays(nums2, nums1)

        start = 0
        end = s1
        midTwoLists = (s1 + s2 + 1) // 2

        while (start <= end):
            mid = (start + end) // 2
            p1Asize = mid
            p1Bsize = midTwoLists - mid

            p1A = nums1[p1Asize - 1] if (p1Asize > 0) else float("-inf")
            p1B = nums2[p1Bsize - 1] if (p1Bsize > 0) else float("-inf")
            p2A = nums1[p1Asize] if (p1Asize < s1) else float("inf")
            p2B = nums2[p1Bsize] if (p1Bsize < s2) else float("inf")

            if p1A <= p2B and p1B <= p2A:
                if (s1 + s2) % 2 == 0:
                    return (max(p1A, p1B) + min(p2A, p2B)) / 2
                return max(p1A, p1B)

            elif (p1A > p2B):
                end = mid - 1
            else:
                start = mid + 1