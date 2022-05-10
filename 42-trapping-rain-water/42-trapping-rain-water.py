class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # calculate maximum on the left, and on the right at each position
        max_left = [0 for _ in range(n)]
        max_right = [0 for _ in range(n)]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        # calculate amount of money on top of each elevation
        amount_water = 0
        for i in range(n):
            top = min(max_left[i], max_right[i]) - height[i]
            if top > 0:
                amount_water += top
        return amount_water
    
    # Solution with stack, time limit exceeded but it works
    """
    # from collections import defaultdict
    def sort_last(self, L: List[int]) -> None:  # sort a sorted list with an item added at the end
        n = len(L)
        j = n - 1
        while (j > 0) and (L[j] < L[j-1]):
            L[j], L[j-1] = L[j-1], L[j]
            j -= 1
    
    def trap(self, height: List[int]) -> int:
        trapped = 0  # water trapped
        pos = defaultdict(list)  # dictionnary, map each heigh to a list of position
        max_height = 0  # max elevation
        for i, h in enumerate(height):
            pos[h].append(i)
            max_height = max(max_height, h)
        for h in pos:
            pos[h].sort()  # sort by x-axis

        while pos and (max_height > 0):
            if len(pos[max_height]) < 2:  # decrease the height until we have at least two elevations with same height (to have water between them)
                new_max_height = max_height-1
                while not(pos[new_max_height]) and (new_max_height > 0):
                    new_max_height -= 1
                pos[new_max_height].extend(pos.pop(max_height))
                max_height = new_max_height
                self.sort_last(pos[max_height])  # sort after having added an item
            else:  # calculate the water between them, decrease the right most elevation
                i_right = pos[max_height].pop()
                i_left = pos[max_height][-1]
                # only decrease the right most elevation
                trapped += (i_right - i_left - 1)
                pos[max_height-1].append(i_right)
                self.sort_last(pos[max_height-1])  # sort after having added an item

        return trapped
    """
