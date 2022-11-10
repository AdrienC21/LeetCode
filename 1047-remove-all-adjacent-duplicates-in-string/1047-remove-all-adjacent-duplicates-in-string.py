class Solution:
    def removeDuplicates(self, s: str) -> str:
        d = deque()
        for c in s:
            if d and (d[-1] == c):
                d.pop()
            else:
                d.append(c)
        return "".join(d)
