class Solution:
    def hour(self, n: int) -> str:
        if n == 0:
            return ["0"]
        elif n == 1:
            return ["8", "4", "2", "1"]
        elif n == 2:
            return ["10", "9", "6", "5", "3"]
        else:  # n=3
            return ["11", "7"]
    def minute(self, n: int) -> str:
        if n == 0:
            return ["00"]  # 1
        elif n == 1:
            return ["01", "02", "04", "08", "16", "32"]  # 6
        elif n == 2:
            return ["03", "05", "09", "17", "33", "06",
                    "10", "18", "34", "12", "20", "36",
                    "24", "40", "48"]  # 15
        elif n == 3:
            return ["07", "11", "19", "35", "13", "21", "37",
                    "25", "41", "49", "14", "22", "38", "26",
                    "42", "50", "28", "44", "52", "56"]  # 20
        elif n == 4:
            return ["15", "23", "39", "27", "43", "51", "29",
                    "45", "53", "57", "30", "46", "54", "58"]  # 14
        else:  # n=5
            return ["31", "47", "55", "59"]  # 4
            
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ["0:00"]
        elif turnedOn > 8:
            return []
        else:
            res = []
            for i in range(min(4, turnedOn+1)):
                j = turnedOn - i
                if j < 6:
                    hourList = self.hour(i)
                    minList = self.minute(j)
                    for h in hourList:
                        for m in minList:
                            res.append(f"{h}:{m}")
            return res