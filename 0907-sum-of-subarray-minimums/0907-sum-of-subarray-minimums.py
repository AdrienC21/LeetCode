class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = []
        left_arr = n * [0]
        right = []
        right_arr = n * [0]
        for i in range(n):  # number of time arr[i] is minimum and last element of subarray
            count = 1
            while left and (arr[i] < left[-1][0]):
                count += left.pop()[1]
            left.append((arr[i], count))
            left_arr[i] = count
        for i in range(n-1, -1, -1):  # number of time arr[i] is minimum and first element of subarray
            count = 1
            while right and (arr[i] <= right[-1][0]):
                count += right.pop()[1]
            right.append((arr[i], count))
            right_arr[i] = count
        res = 0
        for i in range(n):  # sum of (number of times arr[i] is minimum) * arr[i]
            res += arr[i] * left_arr[i] * right_arr[i]
        return res % (10**9 + 7)
    
    # TLE, O(1) space but O(n^2) time
    """
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        modulo = 10**9 + 7
        running_min = 0  # init
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    running_min = arr[i]
                    res += arr[i]
                    res %= modulo
                else:
                    running_min = min(running_min, arr[j])
                    res += running_min
                    res %= modulo
        return res
    """
