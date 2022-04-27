from math import sqrt
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        s = sqrt(area)
        if s == int(s):
            return [int(s), int(s)]
        s = int(s)
        for nb in range(s, 0, -1):
            if area % nb == 0:
                return [area // nb, nb]