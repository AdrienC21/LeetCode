class Solution:
    # first idea, implement tries, but not optimal
    
    # Better idea:
    # - a is universal for words2=["aabe", "ccee"] if a as at least "aabccee"
    # - words are 10 letters long, so if upper word for words2 has a length greater than 10, return []
    # - iterate over words1, if len is greater than the top word, don't take into account this word
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # top word of words 2
        freqs = 26 * [0]
        ref = ord("a")
        for w in words2:
            new_freqs = 26 * [0]
            for c in w:
                new_freqs[ord(c) - ref] += 1
            for i in range(26):
                freqs[i] = max(freqs[i], new_freqs[i])
        
        # check early leave
        len_top_word = 0
        for f in freqs:
            if f:
                len_top_word += 1
        if len_top_word > 10:
            return []

        # iterate words1
        res = []
        for w in words1:
            if len(w) < len_top_word:
                continue
            new_freqs = 26 * [0]
            for c in w:
                new_freqs[ord(c) - ref] += 1
            for i in range(26):
                if new_freqs[i] < freqs[i]:
                    break
            else:
                res.append(w)
        return res
