class WordFilter:
    def __init__(self, words: List[str]):
        self.d = {}        
        for index, w in enumerate(words):
            for i in range(len(w)):
                prefix = w[:(i+1)]
                if not(prefix in self.d):
                    self.d[prefix] = {}
                for k in range(len(w)):
                    suffix = w[k:]
                    self.d[prefix][suffix] = index  # max index
        
    def f(self, prefix: str, suffix: str) -> int: 
        if not(prefix in self.d):
            return -1
        if not(suffix in self.d[prefix]):
            return -1
        return self.d[prefix][suffix]
    """
    def __init__(self, words: List[str]):
        indexes = list(range(len(words)))
        s = sorted(zip(words, indexes))
        prefix_words = [t[0] for t in s]
        prefix_indexes = [t[1] for t in s]
        self.prefix_words = prefix_words
        self.prefix_indexes = prefix_indexes
        indexes = list(range(len(words)))
        inverted_words = [w[::-1] for w in words]
        s = sorted(zip(inverted_words, indexes))
        suffix_words = [t[0] for t in s]
        suffix_indexes = [t[1] for t in s]
        self.suffix_words = suffix_words
        self.suffix_indexes = suffix_indexes
        self.
    def f(self, prefix: str, suffix: str) -> int: 
    """

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)