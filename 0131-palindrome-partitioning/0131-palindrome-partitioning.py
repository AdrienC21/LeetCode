class Solution:
    def is_palindrome(self, s: str) -> bool:
        # check if substring is a palindrome
        for i in range(len(s) // 2):
            if s[i] != s[-(i+1)]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        # recursive function
        def recSearch(s: str, i: int, path: List[str]) -> None:
            nonlocal res
            if i == n:
                res.append(path)
                return None

            for j in range(i, n):
                if self.is_palindrome(s[i:j+1]):
                    recSearch(s, j + 1, path + [s[i:j+1]])

        recSearch(s, 0, [])
        return res
