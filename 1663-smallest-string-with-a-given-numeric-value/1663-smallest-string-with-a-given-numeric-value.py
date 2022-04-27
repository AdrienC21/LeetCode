class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = n * ["a"]
        K = k - n
        for i in range(n-1, -1, -1):
            if K > 0:
                if K >= 25:
                    K -= 25
                    res[i] = "z"
                else:
                    res[i] = chr(ord(res[i]) + K)
                    K = 0
                    break
            else:
                break
        
        return "".join(res)