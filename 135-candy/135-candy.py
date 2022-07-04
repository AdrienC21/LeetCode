class Solution:
    def triangle_sum(self, n: int) -> int:
        return (n * (n + 1)) // 2
    # use slopes!
    # O(n) time, O(1) space!
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        ups = 0
        downs = 0
        prev_diff = 0
        new_diff = 0
        candies = 0
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                new_diff = 1
            elif ratings[i] < ratings[i-1]:
                new_diff = -1
            else:
                new_diff = 0
            if ((prev_diff > 0) and (new_diff == 0)) or ((prev_diff < 0) and (new_diff >= 0)):
                candies += self.triangle_sum(ups) + self.triangle_sum(downs) + max(ups, downs)
                ups, downs = 0, 0
            if new_diff > 0:
                ups += 1
            elif new_diff < 0:
                downs += 1
            else:
                candies += 1
            prev_diff = new_diff
        
        candies += 1 + self.triangle_sum(ups) + self.triangle_sum(downs) + max(ups, downs)
        
        return candies
