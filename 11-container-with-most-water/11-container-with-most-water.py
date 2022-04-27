class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height) - 1
        i = 0
        heighti = height[i]
        heightj = height[j]
        maxArea = (j - i) * min(heighti, heightj)
        while i < j:
            if heighti <= heightj:
                i += 1
                heighti = height[i]
            else:
                j -= 1
                heightj = height[j]
            maxArea = max(maxArea, (j - i) * min(heighti, heightj))
        return maxArea