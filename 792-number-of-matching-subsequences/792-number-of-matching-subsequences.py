from collections import defaultdict
class Solution:
    # hashmap that store index position
    
    def match(self, s: str, word: str, hashmap: Dict[chr, List[str]], start_pos: int) -> bool:
        if not(word):  # empty word is subsequence
            return True
        if not(word[0] in hashmap):  # first letter not in
            return False
        for pos in hashmap.get(word[0]):
            if pos < start_pos:
                continue
            next_pos_word = word[1:]  # move from one position
            return self.match(s, next_pos_word, hashmap, pos + 1)
        return False

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        hashmap = defaultdict(list)
        for i, c in enumerate(s):
            hashmap[c].append(i)
        for w in words:
            if self.match(s, w, hashmap, 0):
                count += 1
        return count
