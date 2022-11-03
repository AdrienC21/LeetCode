class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = defaultdict(int)
        longest = 0
        for w in words:
            if dic[w[::-1]]:
                dic[w[::-1]] -= 1
                longest += 4
                if w == w[::-1]:
                    dic["reverse"] -= 1
            else:
                dic[w] += 1
                if w == w[::-1]:
                    dic["reverse"] += 1
        if dic["reverse"]:  # one unpaired parallel word like "gg" than can be added at the middle
            longest += 2
        return longest
