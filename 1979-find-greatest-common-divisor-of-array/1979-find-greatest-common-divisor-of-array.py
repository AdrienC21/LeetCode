class Solution:
    def pgcd(self, a: int, b: int) -> int:
        if a < b:
            return self.pgcd(b, a)
        if b == 0:
            return a
        return self.pgcd(b, a % b)
    def findGCD(self, nums: List[int]) -> int:
        min_elt = nums[0]
        max_elt = nums[0]
        for elt in nums[1:]:
            if elt < min_elt:
                min_elt = elt
            if elt > max_elt:
                max_elt = elt
        return self.pgcd(max_elt, min_elt)
