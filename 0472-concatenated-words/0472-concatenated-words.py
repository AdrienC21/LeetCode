class Solution:
    # set for speed up
    # dict to cache previous results
    # O(n*l^2)? where n len(words) and l max len of a word?
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        allwords = set(words)
        calculated = {}

        def is_concatenated(w: str) -> bool:
            nonlocal allwords, calculated
            
            if w in calculated:
                return calculated[w]

            for i in range(1, len(w)):
                begin = w[:i]
                end = w[i:]
                if (begin in allwords) and ((end in allwords) or is_concatenated(end)):
                    return True
            return False

        return [w for w in allwords if is_concatenated(w)]
