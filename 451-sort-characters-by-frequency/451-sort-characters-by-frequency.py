class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        res = ""
        for c, nb in counter.most_common():
            res = res + nb * c
        return res