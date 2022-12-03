class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        freq = c.most_common()
        res = ""
        for (letter, count) in freq:
            res += count * letter
        return res
