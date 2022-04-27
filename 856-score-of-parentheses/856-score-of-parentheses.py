class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if s == "()":
            return 1
        else:
            count = 0
            for i, v in enumerate(s):
                if v == "(":
                    count += 1
                else:
                    count -= 1
                if not(count):
                    if i == (len(s) - 1):
                        return 2 * self.scoreOfParentheses(s[1:-1])
                    else:
                        return self.scoreOfParentheses(s[:(i+1)]) + self.scoreOfParentheses(s[(i+1):])