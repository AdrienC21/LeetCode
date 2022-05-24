class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longestParentheses = 0
        stack = []
        stack.append(-1)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not(stack):
                    stack.append(i)
                longestParentheses = max(longestParentheses, i - stack[-1])
        return longestParentheses
