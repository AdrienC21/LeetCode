class Solution:
    def slope(self, p1: List[int], p2: List[int]) -> float:
        if p1[0] == p2[0]:
            return sys.maxsize
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = self.slope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)):
            if self.slope(coordinates[0], coordinates[i]) != slope:
                return False
        return True
