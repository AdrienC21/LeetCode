class Solution:
    def lexico_order(self, w1: str, w2: str, alien_dict: Dict[str, int]) -> bool:
        for i in range(min(len(w1), len(w2))):
            if alien_dict[w1[i]] > alien_dict[w2[i]]:
                return False
            if alien_dict[w1[i]] < alien_dict[w2[i]]:
                return True
        return len(w1) <= len(w2)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            if not(self.lexico_order(words[i], words[i+1], alien_dict)):
                return False
        return True
