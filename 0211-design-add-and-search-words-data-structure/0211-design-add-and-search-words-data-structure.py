class WordDictionary:

    def __init__(self):
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        trie = self.trie
        for w in word:
            if not(w) in trie:
                trie[w] = {}
            trie = trie[w]
        trie["_end"] = {}

    def recSearch(self, word: str, trie: dict) -> bool:
        for i, w in enumerate(word):
            if w == ".":
                for c in trie:
                    if self.recSearch(word[i+1:], trie[c]):
                        return True
                return False
            else:
                if w not in trie:
                    return False
                trie = trie[w]
        return "_end" in trie

    def search(self, word: str) -> bool:
        return self.recSearch(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)