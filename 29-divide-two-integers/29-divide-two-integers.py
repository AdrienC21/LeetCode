class Solution:
    # bit manipulation
    def divide(self, dividend: int, divisor: int) -> int:
        if not(dividend):
            return 0
        if divisor == 1:
            # check 32 bit integers
            if dividend > (2**31 - 1):
                return (2**31 - 1)
            if dividend < -(2**31):
                return -(2**31)
            return dividend
        if divisor == -1:
            if -dividend > (2**31 - 1):
                return (2**31 - 1)
            if -dividend < -(2**31):
                return -(2**31)
            return -dividend
        if (dividend < 0) and (divisor < 0):
            return self.divide(-dividend, -divisor)
        if dividend < 0:
            return -self.divide(-dividend, divisor)
        if divisor < 0:
            return -self.divide(dividend, -divisor)
        
        res = 0  # result is the quotient
        k = 0
        for i in range(31, -1, -1):  # each bit
            if (k + (divisor << i)) <= dividend:
                k += divisor << i
                res |= 1 << i
        # check 32 bit integers
        if res > (2**31 - 1):
            return (2**31 - 1)
        if res < -(2**31):
            return -(2**31)
        return res
        
    # solution without bit manipulation, time limit exceeded but it work
    """
    def divide(self, dividend: int, divisor: int) -> int:
        if not(dividend):
            return 0
        if divisor == 1:
            # check 32 bit integers
            if dividend > (2**31 - 1):
                return (2**31 - 1)
            if dividend < -(2**31):
                return -(2**31)
            return dividend
        if divisor == -1:
            if -dividend > (2**31 - 1):
                return (2**31 - 1)
            if -dividend < -(2**31):
                return -(2**31)
            return -dividend
        if (dividend < 0) and (divisor < 0):
            return self.divide(-dividend, -divisor)
        if dividend < 0:
            return -self.divide(-dividend, divisor)
        if divisor < 0:
            return -self.divide(dividend, -divisor)
        # now we have only non negative integers
        res = 0
        while dividend >= divisor:
            dividend -= divisor
            res += 1
        # check 32 bit integers
        if res > (2**31 - 1):
            return (2**31 - 1)
        if res < -(2**31):
            return -(2**31)
        return res
    """