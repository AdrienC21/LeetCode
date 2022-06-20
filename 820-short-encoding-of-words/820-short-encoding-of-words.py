class Solution:
    # no trie, to much computation time. No brute force. Trick: remove the words from a set!
    def minimumLengthEncoding(self, words: List[str]) -> int:
        _set = set(words)
        for word in words:
            if word in _set:
                for i in range(1, len(word)):  # for time, remove ime, me, e!
                    _set.discard(word[i:])
        return len("#".join(list(_set)) + "#")  # hastag at the end
