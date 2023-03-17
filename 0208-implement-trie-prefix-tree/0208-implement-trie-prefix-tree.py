class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        root = self.trie
        for w in word:
            if w not in root:
                root[w] = {}
            root = root[w]
        root["_end"] = {}

    def search(self, word: str) -> bool:
        root = self.trie
        for w in word:
            if w not in root:
                return False
            root = root[w]
        return "_end" in root

    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        for w in prefix:
            if w not in root:
                return False
            root = root[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)