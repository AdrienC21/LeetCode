from collections import defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = defaultdict(int)  # frequency of each letter
        for c in s:
            freq[c] += 1
        count = defaultdict(int)  # number of letters per frequence
        for f in freq.values():
            count[f] += 1

        double_frequencies = True
        number_deletions = 0
        while double_frequencies:
            double_frequencies = False
            for f in list(count.keys()):
                if (f != 0) and (count[f] >= 2):
                    double_frequencies = True
                    number_deletions += (count[f] - 1)
                    count[f-1] += (count[f] - 1)
                    count[f] = 1
        return number_deletions
