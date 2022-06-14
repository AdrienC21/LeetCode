class Solution:
    # dynamic programming with only two lines: O(|w2|) in space!
    # O(|w1|*|w2|). Longest common subsequence
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)
        len_w2 = len(word2)
        if len_w1 < len_w2:  # biggest word first
            return self.minDistance(word2, word1)
        dp_final = (len_w2 + 1) * [0]
        dp = (len_w2 + 1) * [0]
        for c1 in word1:
            for j in range(len_w2):
                if c1 == word2[j]:
                    dp[j+1] = dp_final[j] + 1  # previous max + 1
                else:
                    dp[j+1] = max(dp[j], dp_final[j+1])  # old max j+1 or current max on this iteration
            dp_final, dp = dp, dp_final  # update dp_final
        # return number of letters to delete
        return len_w1 + len_w2 - 2 * dp_final[len_w2]
    # failed again ... "sea" and "ate", letters not in the right order
    # O(|w1| + |w2|) we need the number of letters in common. Use a counter hashmap
    """
from collections import defaultdict
    def minDistance(self, word1: str, word2: str) -> int:
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        for c in word1:
            c1[c] += 1
        for c in word2:
            c2[c] += 1
        res = {}
        for key in c1:
            res[key] = min(c1[key], c2[key])
        for key in c2:
            res[key] = min(c1[key], c2[key])
        letters_to_keep = 0
        for key in res:
            letters_to_keep += res[key]
        return len(word1) + len(word2) - 2 * letters_to_keep
    """
    # solution but not for the right problem ... I thought we need to compare substrings ...
    """
import sys
    def calculate_steps(self, w1: str, w2: str, i: int, len_w1: int, len_w2: int) -> int:
        max_letters_common = 0
        letters_common = 0
        for j in range(len_w2):
            if (i + j) >= len_w1:
                break
            if w1[i+j] == w2[j]:
                letters_common += 1
            else:
                max_letters_common = max(max_letters_common, letters_common)
                letters_common = 0
        max_letters_common = max(max_letters_common, letters_common)
        return len_w1 + len_w2 - 2 * max_letters_common
        
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)
        len_w2 = len(word2)
        if len_w1 < len_w2:  # bigger word first (like example 2)
            return self.minDistance(word2, word1)
        min_step = sys.maxsize
        for i in range(len_w1):
            min_step = min(min_step, self.calculate_steps(word1, word2, i, len_w1, len_w2))
        return min_step
    """
