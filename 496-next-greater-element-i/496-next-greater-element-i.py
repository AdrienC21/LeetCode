class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i, v in enumerate(nums2):
            d[v] = i
        
        ans = []
        n = len(nums2)
        for v in nums1:
            j = d[v] + 1
            while (j < n) and (nums2[j] < v):
                j += 1
            if j == n:
                ans.append(-1)
            else:
                ans.append(nums2[j])
        return ans