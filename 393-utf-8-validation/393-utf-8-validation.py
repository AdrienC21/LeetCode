class Solution:
    def is_valid(self, data: List[str]) -> bool:
        i = 0
        while i < len(data):
            if data[i][0] == "0":
                i += 1
            elif data[i][:2] == "10":
                return False
            elif data[i][:3] == "110":
                if ((i + 1) >= len(data)) or (data[i+1][:2] != "10"):
                    return False
                i += 2
            elif data[i][:4] == "1110":
                if ((i + 2) >= len(data)) or (data[i+1][:2] != "10") or (data[i+2][:2] != "10"):
                    return False
                i += 3
            elif data[i][:5] == "11110":
                if ((i + 3) >= len(data)) or (data[i+1][:2] != "10") or (data[i+2][:2] != "10") or (data[i+3][:2] != "10"):
                    return False
                i += 4
            else:
                return False
        return True

    def validUtf8(self, data: List[int]) -> bool:
        # convert integers to bits
        data = ["{0:b}".format(x) for x in data]
        for i, x in enumerate(data):
            data[i] = (8 - len(x)) * "0" + x
        return self.is_valid(data)
