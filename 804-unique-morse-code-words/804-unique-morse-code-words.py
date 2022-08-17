class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        tab = {}
        for i, code in enumerate([".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]):
            tab[chr(ord("a") + i)] = code
        transfo = set()
        for w in words:
            t = []
            for c in w:
                t.append(tab[c])
            transfo.add("".join(t))
        return len(transfo)