class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        max_h = 0
        max_w = 0
        for i in range(len(horizontalCuts)-1):
            if (horizontalCuts[i+1] - horizontalCuts[i]) > max_h:
                max_h = (horizontalCuts[i+1] - horizontalCuts[i])
        for i in range(len(verticalCuts)-1):
            if (verticalCuts[i+1] - verticalCuts[i]) > max_w:
                max_w = (verticalCuts[i+1] - verticalCuts[i])
        return (max_h * max_w) % (10**9 + 7)
