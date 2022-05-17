class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        n = len(citations)
        if citations[0] >= n:  # we are limited by the number of papers
            return n
        for i in range(n):
            if n <= citations[i]:
                return n
            n -= 1
        return n