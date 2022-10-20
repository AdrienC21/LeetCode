class Solution:
    def recConvert(self, num: int) -> List[str]:
        if num >= 1000:
            return (num // 1000) * ["M"] + self.recConvert(num % 1000)
        if num >= 900:
            return ["CM"] + self.recConvert(num - 900)
        if num >= 500:
            return ["D"] + self.recConvert(num - 500)
        if num >= 400:
            return ["CD"] + self.recConvert(num - 400)
        if num >= 100:
            return (num // 100) * ["C"] + self.recConvert(num % 100)
        if num >= 90:
            return ["XC"] + self.recConvert(num - 90)
        if num >= 50:
            return ["L"] + self.recConvert(num - 50)
        if num >= 40:
            return ["XL"] + self.recConvert(num - 40)
        if num >= 10:
            return (num // 10) * ["X"] + self.recConvert(num % 10)
        if num == 9:
            return ["IX"]
        if num == 8:
            return ["VIII"]
        if num == 7:
            return ["VII"]
        if num == 6:
            return ["VI"]
        if num == 5:
            return ["V"]
        if num == 4:
            return ["IV"]
        if num == 3:
            return ["III"]
        if num == 2:
            return ["II"]
        if num == 1:
            return ["I"]
        else:
            return [""]
        
    def intToRoman(self, num: int) -> str:
        return "".join(self.recConvert(num))
