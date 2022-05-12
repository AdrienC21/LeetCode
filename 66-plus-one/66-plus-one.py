class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = digits[:]
        for i in range(len(res)-1, -1, -1):
            if res[i] != 9:
                res[i] += 1
                break
            else:
                res[i] = 0
        if res[0] == 0:
            return [1] + res
        return res