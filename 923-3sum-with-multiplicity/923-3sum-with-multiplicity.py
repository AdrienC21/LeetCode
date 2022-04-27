class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        freq = [0 for _ in range(101)]
        K = ((target + 1) // 3)
        res = 0
        for num in arr:
            freq[num] += 1
        for k in range(min(target, 100), K-1, -1):
            remaining = target - k
            half = ((remaining + 1) // 2)
            for j in range(min(remaining, k), half-1, -1):
                i = remaining - j
                x, y, z = freq[i], freq[j], freq[k]
                if i == k:
                    res += x * (x-1) * (x-2) // 6
                elif i == j:
                    res += (z * x * (x-1)) // 2
                elif j == k:
                    res += (x * y * (y-1)) // 2
                else:
                    res += x * y * z
        return res % ((10**9)+7)