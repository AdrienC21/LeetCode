from math import gcd
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity == 0:
            return True
        pgcd = gcd(jug1Capacity, jug2Capacity)
        d = targetCapacity / pgcd
        return (targetCapacity <= (jug1Capacity + jug2Capacity)) and (int(d) == d)