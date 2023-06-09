class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        i = 0
        j = n - 1
        while i < j:
            m = (i + j) // 2
            if letters[m] <= target:
                i = m + 1
            else:
                j = m - 1
        if letters[i] > target:
            return letters[i]
        elif (i < (n - 1)) and (letters[i+1] > target):
            return letters[i+1]
        return letters[0]
