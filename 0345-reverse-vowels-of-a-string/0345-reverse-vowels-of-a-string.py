class Solution:
    def reverseVowels(self, s: str) -> str:
        L = list(s)
        i = 0
        j = len(L) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while i < j:
            if L[i] not in vowels:
                i += 1
            elif L[j] not in vowels:
                j -= 1
            else:
                L[i], L[j] = L[j], L[i]
                i += 1
                j -= 1
        return "".join(L)
