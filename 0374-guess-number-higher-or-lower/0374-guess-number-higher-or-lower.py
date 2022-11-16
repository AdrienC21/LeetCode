# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i = 1
        j = n
        m = (i + j) // 2
        g = guess(m)
        while not(g == 0):  # not found
            if g == -1:
                j = m - 1
            else:
                i = m + 1
            m = (i + j) // 2
            g = guess(m)
        return m
