class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        k_beauty = 0
        for i in range(n-k+1):
            sub_int = int(s[i:i+k])
            if sub_int and ((num % sub_int) == 0):
                k_beauty += 1
        return k_beauty