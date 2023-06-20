class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        if n < window_size:
            return n * [-1]
        res = k * [-1]
        running_sum = sum(nums[:window_size])
        res.append(int(running_sum / window_size))
        for i in range(k+1, n-k):
            running_sum -= nums[i-k-1]
            running_sum += nums[i+k]
            res.append(int(running_sum / window_size))
        res.extend(k * [-1])
        return res
