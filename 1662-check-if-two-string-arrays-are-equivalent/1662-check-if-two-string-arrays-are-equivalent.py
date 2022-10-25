class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if reduce(lambda x, y: x + y, map(lambda x: len(x), word1)) != reduce(lambda x, y: x + y, map(lambda x: len(x), word2)):
            return False
        return "".join(word1) == "".join(word2)
    """
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        j = 0
        leni = len(word1[0])
        lenj = len(word2[0])
        ki = 0
        kj = 0
        while (i < n1) and (j < n2):
            if word1[i][ki] != word2[j][kj]:
                return False
            ki += 1
            if ki == leni:
                ki = 0
                i += 1
                if i < n1:
                    leni = len(word1[i])
            kj += 1
            if kj == lenj:
                kj = 0
                j += 1
                if j < n2:
                    lenj = len(word2[j])
        return (i == n1) and (j == n2)
    """
