class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        to_change_id = None
        nb_diff = 0
        if len(s) != len(goal):
            return False
        for i, c in enumerate(s):
            if c != goal[i]:
                if nb_diff == 2:
                    return False
                if nb_diff == 1:
                    if (s[to_change_id] != goal[i]) or (goal[to_change_id] != s[i]):
                        return False
                    nb_diff += 1
                if not(nb_diff):
                    to_change_id = i
                    nb_diff += 1
        if nb_diff == 1:
            return False
        if not(nb_diff):
            return max(Counter(s).values()) >= 2
        return True
