class Solution:
    def recHex(self, num: int) -> str:
        if num < 16:
            if num < 10:
                return str(num)
            if num == 10:
                return "a"
            if num == 11:
                return "b"
            if num == 12:
                return "c"
            if num == 13:
                return "d"
            if num == 14:
                return "e"
            if num == 15:
                return "f"
        else:
            return self.recHex(num//16) + self.recHex(num % 16)
    def reverse(self, s: str) -> str:
        res = ""
        for c in s:
            if c == "0":
                res = res + "f"
            elif c == "1":
                res = res + "e"
            elif c == "2":
                res = res + "d"
            elif c == "3":
                res = res + "c"
            elif c == "4":
                res = res + "b"
            elif c == "5":
                res = res + "a"
            elif c == "6":
                res = res + "9"
            elif c == "7":
                res = res + "8"
            elif c == "8":
                res = res + "7"
            elif c == "9":
                res = res + "6"
            elif c == "a":
                res = res + "5"
            elif c == "b":
                res = res + "4"
            elif c == "c":
                res = res + "3"
            elif c == "d":
                res = res + "2"
            elif c == "e":
                res = res + "1"
            else:
                res = res + "0"
        return res
    def toHex(self, num: int) -> str:
        if num < 0:
            s = self.recHex(-(num+1))
            n = len(s)
            new_s = (8-n) * "f" + self.reverse(s)
            return new_s
        
        return self.recHex(num)