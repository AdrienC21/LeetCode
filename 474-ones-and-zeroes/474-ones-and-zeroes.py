class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        max_array = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # how many strings to cumulate at most k zeros and l ones
        for i, s in enumerate(strs):
            # count zeros and ones for each word
            nb1 = 0
            nb0 = 0
            for c in s:
                if c == "1":
                    nb1 += 1
                else:
                    nb0 += 1
            # update dynamic programming
            for k in range(m, nb0-1, -1):
                for l in range(n, nb1-1, -1):
                    max_array[k][l] = max(max_array[k][l], max_array[k-nb0][l-nb1] + 1);
        return max_array[m][n]
