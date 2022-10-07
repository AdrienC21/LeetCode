from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.insert(key, value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        L = self.data[key]
        if not(L):
            return ""
        n = len(L)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if L[m][0] == timestamp:
                return L[m][1]
            elif L[m][0] < timestamp:
                i = m + 1
            else:
                j = m - 1
        k = min(i, j)
        l = max(i, j)
        if ((k >= 0) and (k < n) and (L[k][0] <= timestamp)):
            return L[k][1]
        if ((l >= 0) and (l < n) and (L[l][0] <= timestamp)):
            return L[l][1]
        if ((l > 0) and (L[l-1][0] <= timestamp)):
            return L[l-1][1]
        return ""

    def insert(self, key: str, value: str, timestamp: int) -> None:
        L = self.data[key]
        if not(L):
            L.append((timestamp, value))
            return
        n = len(L)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if L[m][0] < timestamp:
                i = m + 1
            else:
                j = m - 1
        if j < 0:
            L.insert(0, (timestamp, value))
        elif (i == (n-1)) and (L[i][0] < timestamp):
            L.insert(n, (timestamp, value))
        else:
            L.insert(i, (timestamp, value))
        self.data[key] = L

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)