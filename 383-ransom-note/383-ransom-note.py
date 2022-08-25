class Solution:
    # version with array instead of dict
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = 26 * [0]
        freq2 = 26 * [0]
        orda = ord("a")
        for c in ransomNote:
            freq1[ord(c) - orda] += 1
        for c in magazine:
            freq2[ord(c) - orda] += 1
        for i in range(26):
            if freq1[i] > freq2[i]:
                return False
        return True

"""
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for c in ransomNote:
            freq1[c] += 1
        for c in magazine:
            freq2[c] += 1
        for c in list(freq1.keys()):
            if c not in freq2:
                return False
            if freq1[c] > freq2[c]:  # not enough c letters in magazine
                return False
        return True

"""
