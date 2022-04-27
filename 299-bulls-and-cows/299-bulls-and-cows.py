class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = list(secret)
        g = list(guess)
        new_s = {}  # frequency of non bulls caracters
        new_g = {}
        bulls = 0
        cows = 0
        for i, c_s in enumerate(s):
            c_g = g[i]
            if c_s == c_g:
                bulls += 1
            else:
                new_s[c_s] = new_s.get(c_s, 0) + 1
                new_g[c_g] = new_g.get(c_g, 0) + 1
        for c in new_g:
            if c in new_s:
                cows += min(new_s[c], new_g[c])
        return f"{bulls}A{cows}B"