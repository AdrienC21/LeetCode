class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [((candie + extraCandies) >= max(candies)) for candie in candies]
