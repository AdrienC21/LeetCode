class Solution:
    def rom(self, n: int, s: str, len_s: int):
        if len_s == 0:
            return (n, "", 0)
        elif len_s == 1:
            if s[0] == "M":
                return (n + 1000, "", 0)
            elif s[0] == "D":
                return (n + 500, "", 0)
            elif s[0] == "C":
                return (n + 100, "", 0)
            elif s[0] == "L":
                return (n + 50, "", 0)
            elif s[0] == "X":
                return (n + 10, "", 0)
            elif s[0] == "V":
                return (n + 5, "", 0)
            elif s[0] == "I":
                return (n + 1, "", 0)
        else:
            if s[0] == "M":
                return self.rom(n + 1000, s[1:], len_s - 1)
            elif s[:2] == "CM":
                return self.rom(n + 900, s[2:], len_s - 2)
            elif s[0] == "D":
                return self.rom(n + 500, s[1:], len_s - 1)
            elif s[:2] == "CD":
                return self.rom(n + 400, s[2:], len_s - 2)
            elif s[0] == "C":
                return self.rom(n + 100, s[1:], len_s - 1)
            elif s[:2] == "XC":
                return self.rom(n + 90, s[2:], len_s - 2)
            elif s[0] == "L":
                return self.rom(n + 50, s[1:], len_s - 1)
            elif s[:2] == "XL":
                return self.rom(n + 40, s[2:], len_s - 2)
            elif s[0] == "X":
                return self.rom(n + 10, s[1:], len_s - 1)
            elif s[:2] == "IX":
                return self.rom(n + 9, s[2:], len_s - 2)
            elif s[0] == "V":
                return self.rom(n + 5, s[1:], len_s - 1)
            elif s[:2] == "IV":
                return self.rom(n + 4, s[2:], len_s - 2)
            elif s[0] == "I":
                return self.rom(n + 1, s[1:], len_s - 1)
            else:
                raise ValueError("Error?")
            
    def romanToInt(self, s: str) -> int:
        (n, _, _) = self.rom(0, s, len(s))
        return n