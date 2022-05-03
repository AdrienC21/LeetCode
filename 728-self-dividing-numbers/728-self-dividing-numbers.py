class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for x in range(left, right+1):
            str_x = str(x)
            if not("0" in str_x):
                is_self_dividing = True
                i = 0
                n = len(str_x)
                while is_self_dividing and (i < n):
                    is_self_dividing = ((x % int(str_x[i])) == 0)
                    i += 1
                if is_self_dividing:
                    res.append(x)
        return res