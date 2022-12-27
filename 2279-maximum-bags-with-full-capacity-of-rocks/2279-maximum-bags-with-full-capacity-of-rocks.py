class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = sorted([c - r for c, r in zip(capacity, rocks)])
        for i, r in enumerate(remaining):
            if r <= additionalRocks:
                additionalRocks -= r
            else:
                return i
        return len(remaining)
