class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        n = len(timeSeries)
        for i in range(n-1):
            if (timeSeries[i] + duration) < timeSeries[i+1]:
                res += duration
            else:
                res += (timeSeries[i+1] - timeSeries[i])
                
        res += duration  # last attack
        return res