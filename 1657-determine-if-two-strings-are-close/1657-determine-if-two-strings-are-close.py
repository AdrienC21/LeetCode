from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):  # not same length
            return False
        if set(word1) != set(word2):  # not same letters
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # return True if we can order in both words:
        # aaabbbbccd... = aaabbbbccd...
        # now that we have the same letters, we need the same counts
        # => sort before comparing
        return sorted(freq1.values()) == sorted(freq2.values())
