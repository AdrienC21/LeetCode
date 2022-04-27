class Solution:
    def recCombi(self, digits: str, dicPhone: dict) -> List[str]:
        if digits == "":
            return []
        if len(digits) == 1:
            return dicPhone[digits[0]]
        L = dicPhone[digits[0]]
        subRes = self.recCombi(digits[1:], dicPhone)
        res = []
        for w in subRes:
            for letter in L:
                res.append(letter + w)
        return res
        
    def letterCombinations(self, digits: str) -> List[str]:
        dicPhone = {"2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}
        return self.recCombi(digits, dicPhone)