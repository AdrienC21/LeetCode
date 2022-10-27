from scipy.signal import correlate2d
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        corr = correlate2d(img1, img2)
        return corr.max()
