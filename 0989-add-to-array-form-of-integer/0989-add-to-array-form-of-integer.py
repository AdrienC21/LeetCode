class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        power = 1
        final_int = k
        for i in range(len(num)-1, -1, -1):
            final_int += power * num[i]
            power *= 10
        res = []
        while final_int:
            res.append(final_int % 10)
            final_int = final_int // 10
        return res[::-1]
