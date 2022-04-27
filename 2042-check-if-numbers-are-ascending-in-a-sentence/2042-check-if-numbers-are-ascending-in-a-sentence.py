class Solution:
    def is_digit(self, s: str) -> bool:
        for _, c in enumerate(s):
            if not(c.isdigit()):
                return False
        return True
    def areNumbersAscending(self, s: str) -> bool:
        L = s.split(" ")
        L = [x for x in L if self.is_digit(x)]
        L = list(map(lambda x: int(x), L))
        a = L.pop(0)
        for b in L:
            if b <= a:
                return False
            a = b
        return True