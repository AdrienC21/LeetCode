class Solution:
    def convert(self, num: int, d) -> str:  # convert number != 0 and < 1000 to a string
        n = num
        res = []
        j = n // 100
        if j != 0:
            res.append(d[j])
            res.append("Hundred")
        n = n % 100
        if n != 0:
            if (n < 20) or ((n % 10) == 0):
                res.append(d[n])
            else:
                k = 10 * (n // 10)
                res.append(d[k])
                res.append(d[n%10])
        return res
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        n = num
        res = []
        
        packets = [("Billion", 10**9), ("Million", 10**6),
                   ("Thousand", 10**3)]
        
        d = {1: "One",
             2: "Two",
             3: "Three",
             4: "Four",
             5: "Five",
             6: "Six",
             7: "Seven",
             8: "Eight",
             9: "Nine",
             10: "Ten",
             11: "Eleven",
             12: "Twelve",
             13: "Thirteen",
             14: "Fourteen",
             15: "Fifteen",
             16: "Sixteen",
             17: "Seventeen",
             18: "Eighteen",
             19: "Nineteen",
             20: "Twenty",
             30: "Thirty",
             40: "Forty",
             50: "Fifty",
             60: "Sixty",
             70: "Seventy",
             80: "Eighty",
             90: "Ninety"}
        
        for i in range(3):
            name, size = packets[i]
            j = n // size
            if j != 0:
                res.extend(self.convert(j, d))
                res.append(name)
            n = n % size
        
        if n != 0:
            res.extend(self.convert(n, d))
        
        return " ".join(res)