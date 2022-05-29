class Solution:
    def maxProduct(self, words: List[str]) -> int:
        set_l = []
        lenghts = []
        for w in words:
            lenghts.append(len(w))
            set_l.append(set(w))
        n = len(words)
        max_prod = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if not(set_l[i].intersection(set_l[j])):
                    max_prod = max(max_prod, lenghts[i] * lenghts[j])
        return max_prod