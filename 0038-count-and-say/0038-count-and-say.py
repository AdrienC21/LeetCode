class Solution:
    def __init__(self):
        self.calculated = {1: "1"}
    def countAndSay(self, n: int) -> str:
        if n in self.calculated:
            return self.calculated[n]
        prev = self.countAndSay(n-1)
        new_seq = []
        current_letter = '-'
        count = 0
        for i, c in enumerate(prev):
            if c != current_letter:
                new_seq.append(f"{count}{current_letter}")
                count = 1
                current_letter = c
            else:
                count += 1
        new_seq.append(f"{count}{current_letter}")
        new_seq = new_seq[1:]
        self.calculated[n] = "".join(new_seq)
        return self.calculated[n]
