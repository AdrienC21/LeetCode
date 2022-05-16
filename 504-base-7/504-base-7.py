class Solution:
    def recConvert(self, num: int) -> List[str]:
        if num < 7:
            return [str(num)]
        return self.recConvert(num // 7) + [str(num % 7)]
        
    def convertToBase7(self, num: int) -> str:
        L = self.recConvert(abs(num))
        res = "".join(L)
        if num < 0:
            return str(-int(res))
        return res