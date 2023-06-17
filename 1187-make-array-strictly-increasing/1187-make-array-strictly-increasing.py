class Solution:
    # not mine, O((|arr1| + |arr2|) * log(|arr2|))
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {}
        dp[-1] = 0

        len2 = len(arr2)
        arr2.sort()

        for n in arr1:
            next_dp = defaultdict(lambda: sys.maxsize)
            for val, steps in dp.items():
                # keep val in arr1
                if n > val:
                    next_dp[n] = min(next_dp[n], steps)
                # try replace the value with arr2 and increase steps
                i = bisect_right(arr2, val)
                if i < len2:
                    next_dp[arr2[i]] = min(next_dp[arr2[i]], steps + 1)
            if not(next_dp):
                return -1
            dp = next_dp

        return min(dp.values())
